import json, re, os
TODAY = '2026-11-22'
keys = {k['key']: k for k in json.load(open('data/spec_keys.json'))['keys']}
aliases = json.load(open('data/spec_key_aliases.json'))

def pfile(name):
    return 'data/parts/%s.json' % name

def load(f): return json.load(open(f))
def save(f, d, ind=2):
    json.dump(d, open(f, 'w'), ensure_ascii=False, indent=ind); open(f, 'a').write('\n')

GROUP_DEFAULT = {}
def row(key, value, unit='', note='', source='', group=None, label=None, ref=None):
    assert key not in aliases, key
    k = keys.get(key)
    g = group or (k['group'] if k else None)
    assert g, 'group needed for ' + key
    lab = label or (k['label'] if k else key.replace('_', ' ').capitalize())
    r = {'group': g, 'key': key, 'label': lab, 'value': value, 'unit': unit, 'note': note, 'source': source}
    if ref: r['ref'] = ref
    return r

def add_specs(rid, rows, docs, new_file_meta=None):
    f = 'data/specs/%s.json' % rid
    if os.path.exists(f):
        d = load(f)
    else:
        d = {'id': rid, 'checked': TODAY, 'documents': [], 'specs': []}
    have = {(r['key'], str(r['value']), r.get('note', '')) for r in d['specs']}
    n = 0
    for r in rows:
        sig = (r['key'], str(r['value']), r.get('note', ''))
        if sig in have: continue
        # skip exact same key+value already present regardless of note
        if any(x['key'] == r['key'] and str(x['value']) == str(r['value']) for x in d['specs']): continue
        d['specs'].append(r); n += 1
    urls = {x['url'] for x in d['documents']}
    for t, u in docs:
        if u not in urls: d['documents'].append({'title': t, 'url': u})
    d['checked'] = TODAY
    save(f, d, 1)
    return n

def update_rec(file, rid, **kw):
    d = load(pfile(file))
    for r in d:
        if r['id'] == rid:
            for k, v in kw.items():
                if k == 'sources_add':
                    for u in v:
                        r.setdefault('sources', [])
                        if u not in r['sources']: r['sources'].append(u)
                else:
                    r[k] = v
            save(pfile(file), d)
            return
    raise SystemExit('missing ' + rid)

report = {}

# ---- OTTO 100 / 1500
update_rec('amr-agv', 'otto-otto-100', verification='official',
          note='Checked 2026-11-22 against ottomotors.com/100 and its data sheet: 150 kg payload and the standards/marks list match the record.',
          sources_add=['https://ottomotors.com/100/'])
update_rec('amr-agv', 'otto-otto-1500', verification='official',
          note='Checked 2026-11-22 against ottomotors.com/1500 and its data sheet: 1,900 kg payload, 10 h runtime (90% to 10%), 60 min charge (10% to 90%) and the standards list match the record.',
          sources_add=['https://ottomotors.com/1500'])
report['otto-100'] = add_specs('otto-otto-100', [
    row('charge_time', 60, 'minutes', '10% to 90% — verify vs. 100 page: page shows value via script only', 'https://ottomotors.com/100/') ][:0], [('OTTO 100 product page (checked 2026-11-22)', 'https://ottomotors.com/100/')])
report['otto-1500'] = add_specs('otto-otto-1500', [
    row('charge_time', 60, 'minutes', 'Charge time 10% to 90% (product page key specifications)', 'https://ottomotors.com/1500'),
    row('runtime', 10, 'hours', 'Runtime 90% to 10% (product page key specifications)', 'https://ottomotors.com/1500'),
    row('camera_type', '4 x 3D cameras: two forward-facing, two rear-facing', '', 'Product page "Behind the Chassis"', 'https://ottomotors.com/1500', group='Sensors & Perception'),
    row('lidar_type', '2 corner LiDARs giving a 360° field of view', '', 'Product page "Behind the Chassis"', 'https://ottomotors.com/1500'),
    row('battery_chemistry', 'Lithium-ion', '', 'Product page "Behind the Chassis"', 'https://ottomotors.com/1500'),
], [('OTTO 1500 product page (checked 2026-11-22)', 'https://ottomotors.com/1500')])

# ---- Samhyun BOLDUM
update_rec('amr-agv', 'samhyun-boldum', verification='official',
           note='Checked 2026-11-22 against the Samhyun BOLDUM page: 3 t payload, 5.7 km/h (1.58 m/s), 7° slope, ±20 mm positioning, IP67, -20 to 50 °C. A high-power option (20 km/h, 10° slope) and 5/7/10 t models (planned for 2026) are mentioned but have no full spec table.')
report['boldum'] = add_specs('samhyun-boldum', [
    row('operating_temperature', '-20 to 50', '°C', 'BOLDUM 3 t spec table', 'https://www.samhyun.co.kr/our-up/robot-industry/view?category_code=1210&code=164&tpf=product%2Fview'),
    row('max_speed', 20, 'km/h', 'High-power drive option (page "특장점": 최대속도 20kph, 등판각도 10도 고출력용 옵션)', 'https://www.samhyun.co.kr/our-up/robot-industry/view?category_code=1210&code=164&tpf=product%2Fview'),
    row('planned_variants', '5 t, 7 t and 10 t models planned for 2026', '', 'Page "특장점"/"라인업 확장": 3톤 외 5톤·7톤·10톤까지 단계적 확장 예정', 'https://www.samhyun.co.kr/our-up/robot-industry/view?category_code=1210&code=164&tpf=product%2Fview', group='Identity'),
], [('Samhyun BOLDUM page (re-checked 2026-11-22)', 'https://www.samhyun.co.kr/our-up/robot-industry/view?category_code=1210&code=164&tpf=product%2Fview')])

# ---- Seegrid CR1
update_rec('amr-agv', 'seegrid-lift-cr1', verification='official',
           note='Checked 2026-11-22 against the Seegrid Lift CR1 page: 15 ft lift, 4,000 lb (1,814 kg) payload, 5 mph (2.24 m/s), 5 layered 2D/3D LiDARs, 3 e-stops.')
report['cr1'] = add_specs('seegrid-lift-cr1', [
    row('emergency_stop', '3 emergency stop buttons', '', 'Safety list on product page', 'https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr'),
    row('fork_dimensions', 'ITA rated; 42 in standard, 36-72 in optional', '', 'Key specifications on product page', 'https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr'),
], [('Seegrid Lift CR1 page (re-checked 2026-11-22)', 'https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr')])

# ---- Zebra Freight1500
update_rec('amr-agv', 'zebra-fetch-freight1500', verification='official',
           note='Specs come from Zebra/Fetch Freight500/1500 documents (copyright Zebra, hosted by distributors). Product is Discontinued (Zebra restructuring note, SEC filing 2026). No live maker product page was reachable on 2026-11-22, so no newer values were added.')

# ---- AgiBot A2 Ultra
update_rec('humanoid', 'agibot-a2-ultra', verification='official',
           certifications=['CR (China)', 'CE-MD', 'CE-RED', 'FCC'],
           safety_source='https://www.agibot.com/products/A2_Ultra',
           note='Checked 2026-11-22 against agibot.com/products/A2_Ultra: 169 cm, ~69 kg, 40 DoF, 1.2 m/s, ~2 kg arm load, 1.5 h+ walking / 3 h standing all match. The page also lists A2 Lite (23 DoF, ~64 kg, 0.8 m/s).')
report['a2u'] = add_specs('agibot-a2-ultra', [
    row('certifications', 'CR (China); CE-MD; CE-RED; FCC', '', 'Page: first humanoid to hold top-tier certifications across China, the US and Europe', 'https://www.agibot.com/products/A2_Ultra'),
    row('reliability_test', '1,300 hours continuous walking without anomalies; 92-item full inspection', '', 'Maker claims on product page ("5100 hour walking test" tile, text says up to 1300 hours continuous)', 'https://www.agibot.com/products/A2_Ultra'),
    row('record', 'Guinness World Record: longest distance walked by a humanoid robot, 106.286 km', '', 'Maker claim on product page', 'https://www.agibot.com/products/A2_Ultra', group='Identity', label='Records'),
    row('max_slope', 10, '°', 'Page: climbing 10-degree ramps', 'https://www.agibot.com/products/A2_Ultra'),
], [('AgiBot A2 Ultra product page (re-checked 2026-11-22)', 'https://www.agibot.com/products/A2_Ultra')])

# ---- QUESTER1 (PrimeBOT Q1)
PB = 'https://www.primebot.com/q1.html'
update_rec('humanoid', 'agibot-quester1-q1', verification='official', country='China', locomotion='Legged',
           release_year=2025, status='Commercial', height_mm=880, weight_kg=16, dof=22,
           sdk_available=True, ros_support=True, official_url=PB, sources_add=[PB],
           note='Maker product page is PrimeBOT "启元Q1" (primebot.com/q1.html): 88 cm, about 16 kg with battery, 22 DoF (arm 4x2 + leg 6x2 + waist 2), open SDK/HDK, ROS/ROS2 ecosystem compatible. Unveiled 2025-12-31 by AgiBot co-founder Peng Zhihui; launch coverage quoted ~80 cm, which the product page does not support. agibot.com has no Q1 page.',
           summary='Backpack-sized personal/educational humanoid with 22 compliant joints, open SDK/HDK and ROS/ROS2 compatibility, sold as PrimeBOT Q1.')
report['q1'] = add_specs('agibot-quester1-q1', [
    row('model_number', 'PrimeBOT Q1 (启元Q1) and Q1 Explorer Edition (启元Q1 探索版)', '', 'Two editions listed', PB),
    row('height', 88, 'cm', '"88cm golden height"', PB),
    row('weight_with_battery', 16, 'kg', '"约16kg" including battery', PB),
    row('degrees_of_freedom', 22, '', 'Arm 4x2 + leg 6x2 + waist 2', PB),
    row('dof_per_arm', 4, '', '', PB),
    row('dof_per_leg', 6, '', '', PB),
    row('dof_waist', 2, '', '', PB),
    row('joint_type', 'Quasi-direct-drive (QDD) joints with 22 compliant force-controlled DoF', '', 'Ring-gear motor integrated with housing', PB, group='Actuation & Joints', label='Joint type'),
    row('joint_mass', 260, 'g', 'Powder-metallurgy ring-gear motor + housing, 2.5 mm hollow wiring', PB),
    row('joint_torque_density', 85, 'N·m/kg', 'Peak torque density', PB, group='Actuation & Joints', label='Peak joint torque density'),
    row('external_ports', 'USB Type-A x1; USB Type-C x1; RJ45 x1; power port 12 V/5 A x1', '', 'Expansion interfaces', PB),
    row('sdk', 'Open SDK, HDK and API; PrimeToolkit skill development platform; joint-level motion-control interface; official base locomotion model open-sourced', '', 'Developer section (items marked * on page)', PB),
    row('ros_support', 'Compatible with ROS/ROS2 ecosystem', '', 'Page wording; no package link given', PB),
    row('locomotion_control', 'Mixture-of-experts RL locomotion model with force/position hybrid control (walking, posing, fall recovery, dynamic performance)', '', '', PB, group='Mobility & Performance', label='Locomotion control'),
    row('included_accessories', 'Power adapter; carrying bag (方舟携行包); original battery', '', '', PB),
    row('color', 'Star Gray; Star White; Sakura Pink', '', 'Q1 Explorer Edition colours', PB),
], [('PrimeBOT Q1 product page, overview and specs', PB)])

# ---- Anigon FA-L
AN = 'https://anigon.ch/robot-platform'
LI = 'https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD'
update_rec('humanoid', 'anigon-fa-l', verification='official', locomotion='Wheeled', height_mm=1890, dof=28, max_speed_mps=1.5,
           status='Pilot', official_url='https://anigon.ch/', sources_add=[AN, LI],
           note='Maker site anigon.ch/robot-platform (checked 2026-11-22): 189 cm, 28 DoF (7 per arm), 1.5 m/s max (subject to operating mode and site policy), dual hot-swap batteries. A March 2026 post by an Aimbo co-founder (maker of the Anigon brand) gives 1,870 mm and 166 kg instead; the site value is kept and the post values are separate rows in the full specs.')
report['fal'] = add_specs('anigon-fa-l', [
    row('model_number', 'ANIGON FA-L series', '', '', AN),
    row('height', 189, 'cm', 'Reference specification', AN),
    row('arm_span', 65, 'cm', 'Reference specification', AN),
    row('degrees_of_freedom', 28, '', 'Full body', AN),
    row('dof_per_arm', 7, '', '', AN),
    row('max_speed', 1.5, 'm/s', 'Subject to operating mode and site policy', AN),
    row('battery_swappable', True, '', 'Dual hot-swap battery system', AN),
    row('battery_count', 2, '', 'Dual hot-swap batteries', AN),
    row('continuous_operation', '24/7 with battery rotation, maintenance and duty-cycle planning', '', '', AN, group='Power & Battery', label='Continuous operation'),
    row('joint_sensors', 'Integrated joint torque sensors; full force-controlled compliance', '', '', AN),
    row('holding_brake', 'Electromagnetic holding brake', '', 'Plus sensitive collision detection and response', AN, group='Safety & Compliance', label='Holding brake'),
    row('compute_module', 'Integrated edge compute controller (compute backpack) with separate safety control unit', '', 'Local inference; safety-critical control separated from model execution', AN),
    row('base_type', 'Adaptive lifting mobile base', '', '', AN, group='Mobility & Performance', label='Base type'),
    row('integration_interfaces', 'ERP, MES and WMS interfaces', '', '', AN, group='Connectivity & Interfaces', label='Integration interfaces'),
    row('height', 1870, 'mm', 'Aimbo co-founder post (2026-03-03) — differs from anigon.ch (189 cm)', LI),
    row('weight', 166, 'kg', 'Aimbo co-founder post (2026-03-03); anigon.ch gives no weight', LI),
    row('rated_payload', 6, 'kg', 'Single arm, rated (co-founder post)', LI),
    row('arm_payload_peak', 10, 'kg', 'Single arm, max (co-founder post)', LI),
    row('arm_reach', 650, 'mm', 'Arm reach ≥ 650 mm (co-founder post)', LI, group='Manipulation', label='Arm reach'),
    row('repeatability', 0.1, 'mm', '± value (co-founder post)', LI, group='Manipulation', label='Repeatability'),
    row('max_tcp_speed', 2, 'm/s', 'Max TCP speed (co-founder post)', LI, group='Manipulation', label='Max TCP speed'),
], [('ANIGON FA-L robot platform page', AN), ('Aimbo AG co-founder LinkedIn post, 2026-03-03', LI)])

# ---- Anyverse K15
AV = 'https://anyverse.com/'
GG = 'https://autonews.gasgoo.com/articles/news/chinese-humanoid-robots-enter-european-new-energy-vehicle-manufacturing-facilities-2075593705955053569'
update_rec('humanoid', 'anyverse-dynamics-k15', verification='official', locomotion='Wheeled', dof=32, runtime_h=6,
           compute_tops=1000, compute_source=AV, status='Commercial', official_url=AV, sources_add=[AV, GG],
           note='Maker site anyverse.com (checked 2026-11-22): 32 DoF, 1000+ TOPS compute, 6 h runtime, 2 mm manipulation accuracy, >1.5 m/s end-effector speed, >6 kg single-arm payload. No height, weight or dimensions are published; compute_tops is the "1000+" floor. Status Commercial: second-generation K15 shipping since July 2026 per company announcement as reported by Gasgoo.',
           summary='General-purpose dual-arm wheeled semi-humanoid for factory, service and home tasks, driven by the MWA latent world model.')
report['k15'] = add_specs('anyverse-dynamics-k15', [
    row('degrees_of_freedom', 32, '', 'Maker page lists "32 DOF"', AV),
    row('ai_compute', '1000+', 'TOPS', 'Maker page "1000+ Tops Compute"', AV, group='Compute & Software', label='AI compute'),
    row('runtime', 6, 'hours', 'Maker page "6 hours Battery Runtime"', AV),
    row('positioning_accuracy', 2, 'mm', 'Manipulation accuracy', AV),
    row('end_effector_speed', '>1.5', 'm/s', '', AV, group='Manipulation', label='End-effector speed'),
    row('arm_payload', '>6', 'kg', 'Single arm', AV),
    row('ai_architecture', 'MWA latent world model with end-to-end learning and reinforcement learning; multimodal fusion of vision, tactile and force', '', '', AV, group='Compute & Software', label='AI architecture'),
    row('wrist_flip_radius', 30, 'mm', 'Company figure quoted by Gasgoo', GG, group='Manipulation', label='Wrist flip radius'),
    row('workspace_width', 800, 'mm', 'Omnidirectional workspace width, company figure quoted by Gasgoo', GG, group='Terrain & Navigation Limits', label='Workspace width'),
    row('certifications', 'CE-MD; CE-RED; CE-EMC; EN ISO 13849 (functional safety); EN 18031 (cybersecurity)', '', 'Company announcement of 2026-07-09 as reported by Gasgoo', GG),
], [('Anyverse Dynamics homepage (K15 product section)', AV), ('Gasgoo, 2026-07-10: K15 shipped to Envision France factory', GG)])
d = load(pfile('humanoid'))
for r in d:
    if r['id'] == 'anyverse-dynamics-k15':
        r['certifications'] = ['CE-MD', 'CE-RED', 'CE-EMC', 'EN ISO 13849 (functional safety)', 'EN 18031 (cybersecurity)']
        r['safety_source'] = GG
save(pfile('humanoid'), d)

# ---- Apptronik QDH
AP = 'https://apptronik.com/our-work/qdh'
update_rec('humanoid', 'apptronik-qdh', verification='official', official_url=AP, sources_add=[AP],
           status='Research',
           note='Maker page (checked 2026-11-22) calls QDH an upper-body humanoid platform that can be paired with different mobility bases, a completed predecessor to Apollo; it publishes no height, weight, payload, DoF or runtime. Third-party figures (14 DoF, 165 cm, 73 kg) were not added. Kept as a legged research platform per Apptronik\'s own description as a bipedal mobility platform in its 2023 post.',
           summary='Apptronik\'s Quick Development Humanoid, an early upper-body humanoid platform that preceded Apollo.')
report['qdh'] = add_specs('apptronik-qdh', [
    row('robot_type', 'Upper-body humanoid platform that can be paired with different mobility bases', '', 'Maker project page; past tense — predecessor of Apollo', AP, group='Identity', label='Robot type'),
    row('manufacturer', 'Apptronik', '', '', AP),
], [('Apptronik QDH project page', AP)])
print(report)
