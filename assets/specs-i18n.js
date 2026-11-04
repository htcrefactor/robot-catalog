// Strings for the full-spec views. Same keys per language.
Object.assign(I18N.en,{nav_specs:"All specs",full_specs:"Full specifications",full_specs_sub:"Every spec published for this robot, grouped. {n} values from {d} documents.",
 show_all_fields:"Also show catalog fields this robot doesn't publish",not_published:"Not published",no_full_specs:"Full specifications for this robot are being researched.",
 documents:"Documents",specs_title:"Every spec in the catalog",specs_sub:"The superset of every spec published for any robot here: {k} spec fields across {r} robots. Pick a field to compare every robot that publishes it.",
 coverage:"Robots",field:"Spec field",value:"Value",note:"Note",source:"Source",pick_field:"Pick a spec field",search_fields:"Search spec fields…"});
Object.assign(I18N.ko,{nav_specs:"전체 사양",full_specs:"전체 사양",full_specs_sub:"이 로봇에 대해 공개된 모든 사양을 그룹별로 정리했습니다. 문서 {d}개, 값 {n}개.",
 show_all_fields:"이 로봇이 공개하지 않은 카탈로그 항목도 표시",not_published:"미공개",no_full_specs:"이 로봇의 전체 사양은 조사 중입니다.",
 documents:"문서",specs_title:"카탈로그의 모든 사양",specs_sub:"이 사이트의 모든 로봇에 공개된 사양 항목의 합집합: 로봇 {r}대, 사양 항목 {k}개. 항목을 고르면 그 항목을 공개한 모든 로봇을 비교합니다.",
 coverage:"로봇 수",field:"사양 항목",value:"값",note:"비고",source:"출처",pick_field:"사양 항목을 선택하세요",search_fields:"사양 항목 검색…"});
const GROUP_KO={"Identity":"식별 정보","Dimensions & Mass":"크기 및 무게","Mobility & Performance":"이동 및 성능","Terrain & Navigation Limits":"지형 및 주행 한계","Power & Battery":"전원 및 배터리","Charging & Docking":"충전 및 도킹","Environment & Protection":"환경 및 보호 등급","Sensors & Perception":"센서 및 인지","Compute & Software":"컴퓨팅 및 소프트웨어","Connectivity & Interfaces":"통신 및 인터페이스","Payload & Mounting":"페이로드 및 장착","Manipulation":"매니퓰레이션","Actuation & Joints":"구동 및 관절","Safety & Compliance":"안전 및 인증","Controls & Operation":"제어 및 운용","Audio, Lights & HMI":"음향, 조명 및 HMI","Transport & Storage":"운송 및 보관","Commercial":"판매 정보"};
const GROUPS=Object.keys(GROUP_KO);
const tg=g=>LANG==="ko"&&GROUP_KO[g]?GROUP_KO[g]:g;
const sv=(v,u)=>v===true?t("yes"):v===false?t("no"):(typeof v==="number"?(+v.toFixed(4)).toLocaleString():esc(v))+(u?` ${esc(u)}`:"");
const host=u=>{try{return new URL(u).hostname.replace(/^www\./,"")}catch(e){return u}};
// Explorer: filters, charts, families
Object.assign(I18N.en,{families:"Field families",family:"Related fields compared together",locomotion:I18N.en.locomotion||"Locomotion",category:I18N.en.category||"Category",robot:I18N.en.robot||"Robot",
 filter_count:"{n} of {t} robots in filter",filter_maker:"Filter robots by name or maker…",coverage_line:"{a} of {b} robots in your filter publish this field.",text_only:"{n} give it only as text (in the table)",
 min:"Lowest",median:"Median",max:"Highest",unit:"Unit",view_chart:"Ranked",view_dist:"Distribution",view_scatter:"Versus another field",view_table:"Table",sort_asc:"Smallest first ↑",sort_desc:"Largest first ↓",
 distribution:"Distribution",robots_per_bin:"robots per range",plot_against:"Plot against",scatter_few:"Only {n} robots publish both fields.",not_published_by:"Not published by {n} robots in your filter",
 fam_cov:"{a} of {b} robots in your filter publish at least one of these fields.",proxy_toggle:"Fill gaps with {f} (lower bound)",proxy_short:"lower bound from overall width"});
Object.assign(I18N.ko,{families:"관련 항목 묶음",family:"관련 항목을 함께 비교",locomotion:I18N.ko.locomotion||"이동 방식",category:I18N.ko.category||"분류",robot:I18N.ko.robot||"로봇",
 filter_count:"전체 {t}대 중 {n}대 선택됨",filter_maker:"이름 또는 제조사로 로봇 필터…",coverage_line:"필터에 포함된 로봇 {b}대 중 {a}대가 이 항목을 공개합니다.",text_only:"{n}대는 텍스트로만 표기(표 참조)",
 min:"최솟값",median:"중앙값",max:"최댓값",unit:"단위",view_chart:"순위",view_dist:"분포",view_scatter:"다른 항목과 비교",view_table:"표",sort_asc:"작은 값부터 ↑",sort_desc:"큰 값부터 ↓",
 distribution:"분포",robots_per_bin:"구간별 로봇 수",plot_against:"비교할 항목",scatter_few:"두 항목을 모두 공개한 로봇이 {n}대뿐입니다.",not_published_by:"필터 내 미공개 로봇 {n}대",
 fam_cov:"필터에 포함된 로봇 {b}대 중 {a}대가 이 항목 중 하나 이상을 공개합니다.",proxy_toggle:"빈 값을 {f}(하한값)로 채우기",proxy_short:"전체 폭 기준 하한값"});
