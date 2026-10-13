"""Synthetic revision experiment; no media generated and no savings measured."""
import copy,json
from pathlib import Path
import media_preflight as m

def asset(id,modality,cost,deps=()):
    a={'id':id,'brief_approved':True,'rights_confirmed':True,'depends_on':list(deps),
       'spec':{'modality':modality,'provider':'synthetic','model_version':'v1','settings':{'brief':id},'input_hashes':['a'*64]},
       'estimate':{'cost':cost,'currency':'USD','basis':'invented scenario input'}}
    a['cache']={'key':m.key(a['spec']),'accepted':True,'rights_confirmed':True,'artifact_available':True}
    return a

def run():
    base={'currency':'USD','assets':[asset('voice-1','audio',1),asset('voice-2','audio',1),asset('mesh','3d',4),asset('shot-1','video',5,['mesh']),asset('shot-2','video',5,['mesh']),asset('shot-3','video',5)]}
    scenarios=[('unchanged',None,[]),('one-voice-change','voice-2',['voice-2']),('one-shot-change','shot-3',['shot-3']),('mesh-change','mesh',['mesh','shot-1','shot-2'])]
    results=[]
    for name,changed,expected in scenarios:
        document=copy.deepcopy(base)
        if changed:
            next(a for a in document['assets'] if a['id']==changed)['spec']['settings']['revision']=2
        planned=m.plan(document)
        required=[a['id'] for a in planned['assets'] if a['action']!='reuse']
        assert set(required)==set(expected),(name,required,expected)
        results.append({'scenario':name,'regenerate':required,'expected_regenerate':expected,'assertion_passed':True,'full_regeneration_assumed_cost':21,'selective_generation_assumed_cost':planned['known_planned_generation_cost'],'plan':planned})
    return {'kind':'synthetic dependency experiment','scenarios':results,'actual_generation_cost':None,'render_time':None,'quality_scores':None,
      'limitations':['Invented prices; not provider quotes','No media generated or inspected','Missing planning/review/storage/repair costs','Full regeneration is a deliberately wasteful comparator, not proven typical practice','Conservative upstream invalidation may regenerate outputs that could be retained after review']}

if __name__=='__main__':
    result=run();Path(__file__).with_name('media-revision-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps([{'scenario':r['scenario'],'regenerate':r['regenerate'],'assumed_cost':r['selective_generation_assumed_cost']} for r in result['scenarios']]))
