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
