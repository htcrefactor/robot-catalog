// UI strings. Add a language by adding a block with the same keys and listing it in LANGS.
const LANGS={en:"EN",ko:"KR"};
const I18N={
en:{
 brand:"Robot Catalog",nav_robots:"Robots",nav_dash:"Dashboard",nav_table:"Mega table",
 home_title:"Mobile robot catalog",home_sub:"Wheeled, wheel-legged and legged robots: AMRs, AGVs, humanoids, quadrupeds, delivery robots and development platforms, with sourced specs.",
 robots:"robots",manufacturers:"manufacturers",categories:"categories",search:"Search name or maker…",all:"All",no_match:"No robots match.",
 max_speed:"Max speed",min_speed:"Min speed",payload:"Payload",ip:"IP rating",
 back:"← All robots",not_found:"Robot not found",body_motion:"Body & motion",power_env:"Power & environment",soft_compute:"Software & compute",
 dims:"Dimensions (L × W × H)",weight:"Weight",wheel_d:"Wheel diameter",wheels:"Wheels",dof:"Degrees of freedom",runtime:"Runtime",battery:"Battery",released:"Released",price:"Price",
 api:"API",sdk:"SDK",ros:"ROS",onboard:"On-board compute",compute:"Compute",sensors:"Sensors",sources:"Sources",official:"Official page ↗",other_in:"Other robots in this category",
 summary_lang_note:"",
 dash_title:"Dashboard",dash_sub:"All robots side by side. Robots whose source doesn't state a value are left out of that chart, and the count is shown.",
 all_cats:"All categories",wheel_dist:"Wheel diameter distribution",ip_ratings:"IP ratings",show_pie:"Show as pie",show_bars:"Show as bars",
 speed_range:"Speed range per robot (min to max, m/s)",speed_cat:"Max speed by category (lowest / highest, m/s)",features:"Features: YES / NO",ns_note:"N/S = not stated by the source.",feature_matrix:"Feature matrix",
 n_wheel:"{a} of {b} robots state a wheel diameter.",n_ip:"{a} of {b} robots state an IP rating.",n_speed:"{a} of {b} robots state a max speed. Bars start at the stated minimum speed, or 0 when none is stated.",
 not_stated:"Not stated",robot:"Robot",category:"Category",slowest:"slowest",fastest:"fastest",
 table_title:"Mega table",table_sub:"Every robot and every field. Click a column to sort.",filter:"Filter…",csv:"Download CSV",
 col_maker:"Maker",col_country:"Country",col_loco:"Locomotion",col_status:"Status",col_year:"Year",col_sdkname:"SDK name",col_pricenote:"Price note",
 footer:"Specs come from manufacturer pages and datasheets linked on each robot's page. \"N/S\" = not stated by the source.",updated:"Last updated {d}.",
 theme_dark:"Dark mode",theme_light:"Light mode",yes:"YES",no:"NO",ns:"N/S"
},
ko:{
 brand:"로봇 카탈로그",nav_robots:"로봇",nav_dash:"대시보드",nav_table:"전체 표",
 home_title:"모바일 로봇 카탈로그",home_sub:"바퀴형, 바퀴-다리형, 보행형 로봇: AMR, AGV, 휴머노이드, 4족 보행, 배송 로봇, 개발용 플랫폼의 출처 있는 사양.",
 robots:"대",manufacturers:"제조사",categories:"카테고리",search:"이름 또는 제조사 검색…",all:"전체",no_match:"조건에 맞는 로봇이 없습니다.",
 max_speed:"최고 속도",min_speed:"최저 속도",payload:"가반하중",ip:"IP 등급",
 back:"← 전체 로봇",not_found:"로봇을 찾을 수 없습니다",body_motion:"차체 및 이동",power_env:"전원 및 환경",soft_compute:"소프트웨어 및 컴퓨팅",
 dims:"크기 (L × W × H)",weight:"무게",wheel_d:"바퀴 지름",wheels:"바퀴 수",dof:"자유도",runtime:"구동 시간",battery:"배터리",released:"출시",price:"가격",
 api:"API",sdk:"SDK",ros:"ROS",onboard:"온보드 컴퓨팅",compute:"컴퓨터",sensors:"센서",sources:"출처",official:"공식 페이지 ↗",other_in:"같은 카테고리의 다른 로봇",
 summary_lang_note:"설명은 영어 원문입니다.",
 dash_title:"대시보드",dash_sub:"모든 로봇을 한눈에 비교합니다. 출처에 값이 없는 로봇은 해당 차트에서 제외되며, 개수를 함께 표시합니다.",
 all_cats:"전체 카테고리",wheel_dist:"바퀴 지름 분포",ip_ratings:"IP 등급",show_pie:"원형 차트로 보기",show_bars:"막대 차트로 보기",
 speed_range:"로봇별 속도 범위 (최저~최고, m/s)",speed_cat:"카테고리별 최고 속도 (최저 / 최고, m/s)",features:"기능: YES / NO",ns_note:"N/S = 출처에 명시되지 않음.",feature_matrix:"기능 매트릭스",
 n_wheel:"{b}대 중 {a}대가 바퀴 지름을 공개합니다.",n_ip:"{b}대 중 {a}대가 IP 등급을 공개합니다.",n_speed:"{b}대 중 {a}대가 최고 속도를 공개합니다. 막대는 공개된 최저 속도(없으면 0)에서 시작합니다.",
 not_stated:"미공개",robot:"로봇",category:"카테고리",slowest:"가장 느림",fastest:"가장 빠름",
 table_title:"전체 표",table_sub:"모든 로봇의 모든 항목. 열을 누르면 정렬됩니다.",filter:"필터…",csv:"CSV 다운로드",
 col_maker:"제조사",col_country:"국가",col_loco:"이동 방식",col_status:"상태",col_year:"연도",col_sdkname:"SDK 이름",col_pricenote:"가격 비고",
 footer:"사양은 각 로봇 페이지에 링크된 제조사 페이지와 데이터시트에서 가져왔습니다. \"N/S\" = 출처에 명시되지 않음.",updated:"최종 업데이트 {d}.",
 theme_dark:"다크 모드",theme_light:"라이트 모드",yes:"YES",no:"NO",ns:"N/S"
}};
const VALUE_KO={"AMR":"AMR","AGV":"AGV","Humanoid":"휴머노이드","Quadruped":"4족 보행","Wheel-legged":"바퀴-다리형","Indoor delivery":"실내 배송","Outdoor delivery":"실외 배송","Mobile platform":"모바일 플랫폼",
"Wheeled":"바퀴형","Tracked":"궤도형","Legged":"보행형","Commercial":"상용","Pre-order":"사전 주문","Pilot":"시범 운영","Research":"연구용","Discontinued":"단종","Announced":"발표됨",
"China":"중국","United States":"미국","South Korea":"한국","Switzerland":"스위스","Denmark":"덴마크","Germany":"독일","Japan":"일본","Canada":"캐나다","Norway":"노르웨이","United Kingdom":"영국","Estonia":"에스토니아","Colombia":"콜롬비아","France":"프랑스","Israel":"이스라엘","Netherlands":"네덜란드","Taiwan":"대만"};
