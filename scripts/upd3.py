import json
exec(open('scripts/upd1.py').read().split("report = {}")[0])
b = json.load(open('/tmp/cs/botupyourlife.json'))
def buyl(nameparts):
    for x in b:
        if all(p.lower() in x['name'].lower() for p in nameparts): return 'https://botupyourlife.com/en/robots/%s/' % x['id']
    raise SystemExit('no buyl ' + str(nameparts))

TEMPLATE = {k: None for k in ['id','name','manufacturer','country','category','locomotion','release_year','status','length_mm','width_mm','height_mm','weight_kg','payload_kg','max_speed_mps','min_speed_mps','wheel_diameter_mm','wheel_count','dof','runtime_h','battery_wh','ip_rating','api_support','sdk_available','sdk_name','onboard_compute','compute_detail','ros_support','price_usd','price_note','official_url','summary','image_url','image_source','verification','note']}
def mk(**kw):
    r = dict(TEMPLATE); r['sensors'] = []; r['sources'] = []; r['videos'] = []; r['seen_on'] = []
    r.update(kw); return r

def add_rec(file, rec):
    d = load(pfile(file))
    if any(x['id'] == rec['id'] for x in d): raise SystemExit('dup ' + rec['id'])
    d.append(rec); save(pfile(file), d)

RM = 'Reeman'
F = 'Shenzhen Reeman forklift page'
recs = []
HM = 'https://www.reemanrobot.com/forklift/stackman-1200-autonomous-forklift-trucks.html'
TM = 'https://www.reemanrobot.com/forklift/titan-mini-autonomous-forklift.html'
XA = 'https://www.reemanrobot.com/forklift/x-ant-autonomous-forklift.html'
RH = 'https://www.reemanrobot.com/forklift/rbot30f-autonomous-forklift-trucks-3-0.html'

add_rec('amr-agv', mk(id='reeman-hammer-counterbalanced-autonomous-forklift-2', name='Hammer Counterbalanced Autonomous Forklift 2.0', manufacturer=RM, country='China', category='AMR', locomotion='Wheeled', status='Commercial', payload_kg=1200, official_url=HM, sources=[HM], seen_on=[buyl(['Hammer Counterbalanced'])], verification='official',
    summary='Counterbalanced autonomous pallet forklift with 3D pallet recognition, quick-change battery and automatic charging.',
    note='Maker page states 1.2 t load capacity, 2.5 m lifting height and 1.13 m turning radius (page file name stackman-1200).'))
add_rec('amr-agv', mk(id='reeman-titan-mini-autonomous-forklift', name='Titan Mini Autonomous Forklift', manufacturer=RM, country='China', category='AMR', locomotion='Wheeled', status='Commercial', payload_kg=2000, weight_kg=300, official_url=TM, sources=[TM], seen_on=[buyl(['Titan Mini'])], verification='official',
    summary='Compact autonomous forklift for material cart handling with elevator integration for cross-floor delivery.',
    note='Maker page: 2 T capacity, 300 kg light body, autonomous navigation, elevator integration.'))
add_rec('amr-agv', mk(id='reeman-x-ant-autonomous-forklift', name='X-ant Autonomous Forklift', manufacturer=RM, country='China', category='AMR', locomotion='Wheeled', status='Commercial', payload_kg=2000, official_url=XA, sources=[XA], seen_on=[buyl(['X-ant'])], verification='official',
    sensors=['360° stereo vision', '50 m single-line LiDAR', '3D obstacle-avoidance camera', 'Industrial pallet detection'],
    summary='Compact autonomous forklift with 2-ton capacity, laser SLAM navigation and elevator capability for confined spaces.',
    note='Maker page title reads "X-ant Autonomous Forklift (300KG)"; the 300 kg is not labelled as weight, so weight_kg stays empty. 2-ton load capacity, 1,448 mm turning radius.'))
add_rec('amr-agv', mk(id='reeman-rhinoceros-autonomous-forklift-3', name='Rhinoceros Autonomous Forklift Trucks 3.0', manufacturer=RM, country='China', category='AMR', locomotion='Wheeled', status='Commercial', official_url=RH, sources=[RH], seen_on=[buyl(['Rhinoceros'])], verification='official',
    summary='Reeman autonomous forklift truck (RBOT30F 3.0 line).',
    note='Maker page lists the product (URL slug rbot30f-autonomous-forklift-trucks-3-0) but the fetched text carried no spec table, so spec fields stay empty.'))

AR = 'https://www.agile-robots.com/en/products/humanoid-robots/agile-one-s/'
add_rec('humanoid', mk(id='agile-robots-agile-one-s', name='Agile ONE S', manufacturer='Agile Robots', country='Germany', category='Humanoid', locomotion='Legged', status='Commercial', official_url=AR, sources=[AR], seen_on=[buyl(['Agile ONE S'])], verification='official',
    onboard_compute=True, compute_detail='NVIDIA Jetson Thor + Intel Core i3 N305 base computing module', sensors=['Head RGB-D camera', 'Waist 3D LiDAR', 'Waist RGB-D camera', 'Back RGB-D camera'],
    summary='Open reference humanoid platform with onboard Jetson Thor compute and a choice of four-finger or two-finger hands.',
    note='Maker page gives no height, weight or speed. Hand options: four-finger 9 DoF hand or 1 DoF two-finger gripper.'))
AE = 'https://eng.arobot4all.com/ALICE3'
add_rec('humanoid', mk(id='aeirobot-alice-3', name='ALICE 3', manufacturer='AeiROBOT', country='South Korea', category='Humanoid', locomotion='Legged', height_mm=1440, weight_kg=27.5, dof=27, official_url=AE, sources=[AE], seen_on=[buyl(['ALICE 3'])], verification='official',
    onboard_compute=True, compute_detail='NUC11TNKi7; Jetson AGX Xavier', sensors=['3DM-GX4-25 IMU', 'ZED2i stereo camera', 'RFT82-HA02-E force/torque sensor'],
    summary='Korean research humanoid with human-like proportions: 144 cm, 27.5 kg, 27 DoF.',
    note='Maker spec box: 144 cm / 27.5 kg; 27 DoF = leg 6x2, waist 1, arm 7x2, head 2; says specs vary with options.'))
PK = 'https://www.pudurobotics.com/en/products/kettybot_pro'
add_rec('service', mk(id='pudu-kettybot-pro', name='KettyBot Pro', manufacturer='Pudu Robotics', country='China', category='Indoor service', locomotion='Wheeled', status='Commercial', weight_kg=38, max_speed_mps=1.2, runtime_h=9, official_url=PK, sources=[PK], seen_on=[buyl(['KettyBot Pro'])], verification='official',
    sensors=['360° fisheye lenses', 'Smart tray detection'],
    summary='Restaurant and retail delivery and reception robot with an 18.5-inch advertising display and tray-load detection.',
    note='Maker page: 38 kg, 10 kg per layer, 9 h runtime (no load), cruise speed up to 1.2 m/s, 3.5 h charge, clearance >=52 cm.'))
FX = 'https://www.foxtechrobotics.com/xtron-t170a-bipedal-humanoid-research-platform.html'
add_rec('humanoid', mk(id='foxtech-xtron-t170a', name='XTRON T170A', manufacturer='Foxtech', country='China', category='Humanoid', locomotion='Legged', status='Commercial', official_url=FX, sources=[FX], seen_on=[buyl(['XTRON T170A'])], verification='official',
    summary='Bipedal humanoid research platform from Foxtech.',
    note='Maker page: each arm carries up to 5 kg. No other figures were extracted from the page text, so the remaining fields stay empty.'))

add_specs('reeman-hammer-counterbalanced-autonomous-forklift-2', [
    row('max_payload', 1.2, 't', 'Load capacity', HM), row('max_lift_height', 2.5, 'm', 'Lifting height', HM, group='Payload & Mounting'), row('turning_radius', 1.13, 'm', 'Compact turning radius', HM),
    row('pallet_detection', '3D pallet recognition', '', '', HM, group='Sensors & Perception'), row('battery_swappable', True, '', 'Quick-change battery; automatic charging', HM)],
    [('Reeman Hammer Counterbalanced Autonomous Forklift 2.0 page', HM)])
add_specs('reeman-titan-mini-autonomous-forklift', [
    row('max_payload', 2, 't', '2 T capacity', TM), row('weight', 300, 'kg', '"300kg light body"', TM), row('intended_use', 'Material cart handling; elevator integration for cross-floor delivery', '', '', TM, group='Identity', label='Intended use')],
    [('Reeman Titan Mini Autonomous Forklift page', TM)])
add_specs('reeman-x-ant-autonomous-forklift', [
    row('max_payload', 2, 't', '2-ton load capacity', XA), row('turning_radius', 1448, 'mm', 'In-place rotation', XA),
    row('lidar_type', '50 m single-line LiDAR', '', 'Real-time laser SLAM navigation', XA), row('depth_camera_type', '3D obstacle-avoidance camera; 360° stereo vision', '', '', XA, group='Sensors & Perception'),
    row('pallet_detection', 'Industrial-grade pallet detection; automatic pallet pickup with no coding', '', '', XA, group='Sensors & Perception'),
    row('model_number', 'X-ant Autonomous Forklift (300KG)', '', 'Title as printed on the page', XA)],
    [('Reeman X-ant Autonomous Forklift page', XA)])
add_specs('agile-robots-agile-one-s', [
    row('compute_module', 'NVIDIA Jetson Thor (sensor processing and real-time inference) with Intel Core i3 N305 base computing module', '', '', AR),
    row('camera_type', 'Head RGB-D camera; RGB-D cameras at waist and back', '', '', AR), row('lidar_type', '3D LiDAR at the waist', '', '', AR),
    row('hand_dof', 9, '', 'Agile four-finger dexterous hand option', AR), row('hand_dof', 1, '', 'Two-finger gripper option', AR),
    row('software_stack', 'Open software stack; run the models and frameworks of your choice', '', '', AR, group='Compute & Software', label='Software stack'),
    row('control_method', 'Whole-body control coordinating arms, torso and legs', '', '', AR, group='Controls & Operation', label='Control method')],
    [('Agile ONE S product page', AR)])
add_specs('aeirobot-alice-3', [
    row('height', 144, 'cm', '', AE), row('weight', 27.5, 'kg', '', AE), row('degrees_of_freedom', 27, '', 'Leg 6x2, waist 1, arm 7x2, head 2', AE),
    row('dof_per_leg', 6, '', '', AE), row('dof_per_arm', 7, '', '', AE), row('dof_head', 2, '', '', AE), row('dof_waist', 1, '', '', AE),
    row('computer', 'NUC11TNKi7; Jetson AGX Xavier', '', 'Computing module', AE), row('imu', '3DM-GX4-25', '', '', AE, group='Sensors & Perception'),
    row('camera_type', 'ZED2i', '', '', AE), row('force_torque_sensor', 'RFT82-HA02-E', '', '', AE, group='Sensors & Perception', label='Force/torque sensor')],
    [('AeiROBOT ALICE 3 page', AE)])
add_specs('pudu-kettybot-pro', [
    row('weight', 38, 'kg', '', PK), row('rated_payload', 10, 'kg', 'Per tray layer', PK), row('runtime', 9, 'hours', 'No-load operation', PK), row('max_speed', 1.2, 'm/s', 'Cruise speed, max', PK),
    row('charge_time', 3.5, 'hours', '', PK), row('min_corridor_width', 52, 'cm', 'Clearance >= 52 cm in specific situations', PK), row('display', '18.5-inch advertising display', '', '', PK),
    row('tray_dimensions', '35.20 x 34.01 cm', '', '', PK, group='Payload & Mounting', label='Tray dimensions'), row('tray_height', '24.79 / 25.30 / 22.30 cm', '', 'Per layer', PK, group='Payload & Mounting', label='Tray height'),
    row('camera_type', '360° fisheye lenses; smart tray detection', '', '', PK)],
    [('PUDU KettyBot Pro product page', PK)])
add_specs('foxtech-xtron-t170a', [row('arm_payload', 5, 'kg', 'Each arm up to 5 kg', FX)], [('Foxtech XTRON T170A page', FX)])
add_specs('aeirobot-alice-3', [], [])
print('ok')
