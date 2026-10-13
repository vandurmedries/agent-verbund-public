"""Offline media plan validator. No generation, uploads or automatic spending."""
import argparse, hashlib, json, math

def key(spec):
    return hashlib.sha256(json.dumps(spec,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()

def plan(document):
    assets=document.get('assets',[])
    if not isinstance(assets,list) or len(assets)>500:raise ValueError('assets must be a list of at most 500 items')
    ids=[a.get('id') for a in assets]
    if any(not isinstance(i,str) or not i for i in ids) or len(set(ids))!=len(ids):raise ValueError('Unique nonempty asset IDs required')
    known=set(ids);done=set();rows=[];total=0.;blocked=0;reused=0;unknown=0
    pending=list(assets)
    while pending:
        progressed=False
        for a in list(pending):
            deps=a.get('depends_on',[])
            if not isinstance(deps,list) or any(d not in known for d in deps):raise ValueError('Unknown dependency')
            if not set(deps)<=done:continue
            spec=a.get('spec')
            if not isinstance(spec,dict) or not all(spec.get(k) for k in ('modality','provider','model_version','settings','input_hashes')):raise ValueError('Complete generation specification required')
            if spec['modality'] not in ('video','audio','3d'):raise ValueError('Unsupported modality')
            if not isinstance(spec['input_hashes'],list) or any(not isinstance(x,str) or len(x)!=64 or any(c not in '0123456789abcdef' for c in x) for x in spec['input_hashes']):raise ValueError('SHA256 input hashes required')
            fingerprint=key(spec);cache=a.get('cache',{})
            inherited=any(r['id'] in deps and r['action']=='blocked' for r in rows)
            if inherited or a.get('brief_approved') is not True or a.get('rights_confirmed') is not True:
                action='blocked';blocked+=1
            elif all(r['action']=='reuse' for r in rows if r['id'] in deps) and cache.get('key')==fingerprint and cache.get('accepted') is True and cache.get('rights_confirmed') is True and cache.get('artifact_available') is True:
                action='reuse';reused+=1
            else:action='generate_after_dependency_outputs_verified'
            estimate=a.get('estimate',{});cost=estimate.get('cost');currency=estimate.get('currency')
            if cost is not None and (isinstance(cost,bool) or not isinstance(cost,(int,float)) or not math.isfinite(cost) or cost<0):raise ValueError('Nonnegative finite cost required')
            if cost is not None and currency!=document.get('currency'):raise ValueError('Cannot add different currencies')
            if action not in ('reuse','blocked'):
                if cost is None:unknown+=1
                else:total+=cost
            rows.append({'id':a['id'],'action':action,'cache_key':fingerprint,'depends_on':deps,'planned_generation_cost':cost if action not in ('reuse','blocked') else 0})
            done.add(a['id']);pending.remove(a);progressed=True
        if not progressed:raise ValueError('Cyclic dependencies')
    return {'assets':rows,'reuse_candidates':reused,'blocked_assets':blocked,'known_planned_generation_cost':round(total,6),'currency':document.get('currency'),'unknown_cost_assets':unknown,
        'notice':'Plan only: estimates are supplied, not provider quotes. No actual savings, quality or runtime measured. Rehash changed dependency outputs before generating downstream assets. Reuse decisions require operator review.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('manifest');args=parser.parse_args()
    with open(args.manifest,encoding='utf-8') as f:document=json.load(f)
    print(json.dumps(plan(document),indent=2,ensure_ascii=False))
