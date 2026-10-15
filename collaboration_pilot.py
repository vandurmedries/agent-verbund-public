"""Synthetic mechanism demonstrations, not a measured AI treatment comparison."""
from decimal import Decimal, ROUND_HALF_UP
import json

def finalize(records,mode):
    output=[]
    for record in records:
        value=record['score']
        if value is None:
            if mode=='complete':output.append(dict(record))
            continue
        number=Decimal(str(value));number=max(Decimal(0),min(Decimal(100),number))
        rounded=round(float(number)) if mode=='baseline' else int(number.quantize(Decimal(1),rounding=ROUND_HALF_UP))
        output.append({**record,'final':rounded})
    return output

def invariants(mode):
    sample=[{'name':'a','score':62.5},{'name':'b','score':None}]
    original=json.dumps(sample,sort_keys=True)
    result=finalize(sample,mode)
    return {'comment_round_half_up':result[0]['final']==63,
            'held_out_none_passthrough':len(result)==2 and result[1]==sample[1],
            'held_out_no_input_mutation':json.dumps(sample,sort_keys=True)==original,
            'held_out_boundaries':[x['final'] for x in finalize([{'name':'z','score':0},{'name':'h','score':100}],mode)]==[0,100]}

def content_audit(structured,prose,mapping,reviewer_signoff=False):
    """Explicit evidence span gate; literal matches cannot prove semantic equivalence."""
    missing=[];invalid=[]
    for key,value in structured.items():
        span=mapping.get(key)
        if not span:missing.append(key)
        elif span not in prose:invalid.append(key)
    return {'missing_fact_mappings':missing,'invalid_spans':invalid,
            'ready_for_semantic_review':not missing and not invalid,
            'experiment_allowed':not missing and not invalid and reviewer_signoff is True,
            'semantic_equivalence_verified_by_code':False}

def demo():
    facts={'task':'check API','constraint':'no network','acceptance':'report missing key','source':'fixture-v1'}
    prose='Check API using fixture-v1. No network. Report missing key.'
    mapping={'task':'Check API','constraint':'No network','acceptance':'Report missing key','source':'fixture-v1'}
    incomplete=dict(mapping);incomplete.pop('acceptance')
    return {'scope':'Synthetic local mechanism demonstration, not AI-agent efficacy or market demand',
            'hand_authored_variants':{mode:invariants(mode) for mode in ('baseline','comment_only_fix','complete')},
            'handoff_incomplete':content_audit(facts,prose,incomplete),
            'handoff_complete_unreviewed':content_audit(facts,prose,mapping),
            'limitation':'Held-out checks are public here, so cannot be used as concealed outcomes in a future model study. Use new frozen cases and blinded review.'}

if __name__=='__main__':print(json.dumps(demo(),indent=2))
