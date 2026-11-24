import json
exec(open('scripts/upd1.py').read().split("report = {}")[0])
CY='https://www.careyounews.org/news/articleView.html?idxno=12155'
n=add_specs('waseda-airec',[
 row('degrees_of_freedom',36,'axes','Dry-AIREC prototype; Waseda presentation (T. Miyake, 2026-10-21) as reported by CareYou News (2026-10-25)',CY),
 row('height',1660,'mm','Same presentation; differs from the 154 cm in project materials',CY),
 row('weight',150,'kg','Same presentation',CY),
 row('arm_payload',20,'kg','Per arm, maximum',CY),
 row('runtime',3,'hours','Continuous operation about 3 hours',CY),
 row('joint_sensors','Joint torque sensors; impedance control; gel covering on contact surfaces','', 'Same presentation',CY),
],[('CareYou News: K-AgeTech forum report on AIREC (2026-10-25)',CY)])
print(n)
log=json.load(open('data/specs_recheck_log.json'))
log['rechecks']['waseda-airec']=[{'date':TODAY,'result':'new Waseda presentation figures (2026-10-21, via CareYou News): 1,660 mm, 150 kg, 36 axes, 20 kg per arm, ~3 h; added 6 rows (height conflicts with 154 cm in project materials, summary record unchanged)'}]
log['rechecks']['lg-cloid']=[{'date':TODAY,'result':'no new LG datasheet; LG newsroom still gives only 7-DoF arms, 5-finger hands, tilting torso, wheeled base. Korean press says a bipedal CLOiD (130/170/190 cm variants) is planned for early 2027; not official, not added'}]
json.dump(log,open('data/specs_recheck_log.json','w'),indent=2,ensure_ascii=False)
