"""SQLite job-creation reference fixture. No HTTP server or remote API calls.

Contract: keys are required and scoped to tenant. Replay returns the original
job ID, not byte-identical HTTP responses. Conflicting payload reuse is rejected.
This models one SQLite database, not distributed exactly-once side effects.
"""
from contextlib import closing
import hashlib
import json
import sqlite3
from uuid import uuid4

class RequestError(ValueError):
    def __init__(self,status,message):
        self.status=status
        super().__init__(message)

class JobStore:
    def __init__(self,path):
        self.path=str(path)
        with closing(sqlite3.connect(self.path)) as c,c:
            c.execute('''CREATE TABLE IF NOT EXISTS jobs(
              id TEXT PRIMARY KEY,tenant TEXT NOT NULL,request_key TEXT NOT NULL,
              payload_hash TEXT NOT NULL,UNIQUE(tenant,request_key))''')

    def submit(self,tenant,key,payload,lose_response=False,*,after_insert=None,lock_timeout=5):
        if not isinstance(tenant,str) or not tenant or not isinstance(key,str) or not key:
            raise RequestError(400,'Tenant and idempotency key required')
        digest=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
        with closing(sqlite3.connect(self.path,timeout=lock_timeout)) as c,c:
            c.execute('BEGIN IMMEDIATE')
            job_id=str(uuid4())
            created=c.execute('INSERT OR IGNORE INTO jobs VALUES(?,?,?,?)',(job_id,tenant,key,digest)).rowcount
            if after_insert is not None:after_insert()  # Trusted test hook before commit.
            original=c.execute('SELECT id,payload_hash FROM jobs WHERE tenant=? AND request_key=?',(tenant,key)).fetchone()
            if original[1]!=digest:raise RequestError(409,'Key already used with different payload')
            response={'job_id':original[0],'replayed':not bool(created)}
        # Fault injection is after commit: job exists although caller sees timeout.
        if lose_response:raise TimeoutError('Committed job; response lost')
        return response

    def rows(self):
        with closing(sqlite3.connect(self.path)) as c:
            return c.execute('SELECT id,tenant,request_key,payload_hash FROM jobs').fetchall()
