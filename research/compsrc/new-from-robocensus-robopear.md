# Robocensus and Robopear screening (issue #67)

Fetched on 2026-11-18 and matched against `data/parts/*.json` (records and their `variants`).

| Source | Endpoint | Entries | Snapshot |
|---|---|---|---|
| Robocensus | `https://robocensus.com/api/robots.json` (CC BY 4.0, generated 2026-11-16) | 77 | `research/compsrc/robocensus-2026-11-18.json` |
| Robopear | `https://robopear.com/data/models.json` (CC BY 4.0, generated 2026-11-15) | 241 | `research/compsrc/robopear-2026-11-18.json` |

## Result

| Decision | Robocensus | Robopear | Total |
|---|---|---|---|
| already carried | 62 | 213 | 275 |
| duplicate / variant | 10 | 6 | 16 |
| added | 5 | 13 | 18 |
| added to Misc | 0 | 8 | 8 |
| out of scope | 0 | 1 | 1 |
| **all models** | **77** | **241** | **318** |

26 new records were added (993 -> 1019). No value from either catalog is used: the catalogs only say which models exist.
Every new record is a skeleton with empty specs, `verification: null`, the maker's own page as `official_url` where one exists and the catalog page in `seen_on`.
No photo from either site is used (Robocensus photos are not under its data license).

## How a model was matched

1. Maker and model name were normalised (case, punctuation, diacritics, corporate suffixes such as Robotics/Inc/GmbH, and a maker prefix inside the model name) and compared with every record id and with every entry of every record's `variants`.
2. The match was accepted only when the catalog's own product page agreed with the record — same maker page, a translated or shortened name spelled out in the record's note, or a rebrand the record already documents (e.g. TLibot = Sichuan Tianlian, Jingchu Elf = Jingling, Walker 02 = Xingzhe 2).
3. Everything left was read one by one and either added, put in Misc, or left out with the reason below.

A `seen_on` value is the page that catalog publishes for that model (its model page), the same shape the existing `seen_on` entries use, so `scripts/build_disagreements.py` and the `llms` pages can read them.

## Robocensus (77)

| Model (slug) | Maker | Catalog category | Decision | Record / reason |
|---|---|---|---|---|
| MechDog (`hiwonder-mechdog`) | Hiwonder | quadruped | added | `hiwonder-mechdog` |
| PuppyPi (`hiwonder-puppypi`) | Hiwonder | quadruped | added | `hiwonder-puppypi` |
| ROSPug (`hiwonder-rospug`) | Hiwonder | quadruped | added | `hiwonder-rospug` |
| Mini Pupper 1 (`mangdang-mini-pupper-1`) | MangDang | quadruped | added | `mangdang-mini-pupper-1` — The 1st generation is a separate product from Mini Pupper 2. |
| TNY-360 (`tny-robotics-tny-360`) | TNY Robotics | quadruped | added | `tny-robotics-tny-360` |
| D1 (`agibot-d1`) | AgiBot | quadruped | duplicate / variant | `agibot-d1-pro` — Robocensus's product page is the D1 Pro store page; we carry D1 Pro/Ultra/Max/MaxPro separately. |
| ANYmal (`anybotics-anymal`) | ANYbotics | quadruped | duplicate / variant | `anybotics-anymal-d` — Robocensus lists the ANYmal family landing page; we carry generations B, C, D and X separately. |
| Apollo 2 (`apptronik-apollo`) | Apptronik | humanoid | duplicate / variant | `apptronik-apollo-2` — We carry the current Apollo 2. |
| X30 (`deep-robotics-x30`) | DEEP Robotics | quadruped | duplicate / variant | `deep-robotics-x30-pro` — Robocensus's product page is the X30 page; we carry X30 Pro. |
| TonyPi (`hiwonder-tonypi`) | Hiwonder | humanoid | duplicate / variant | `hiwonder-tonypi-pro` — Both catalogs list the base TonyPi; we carry the current TonyPi Pro. |
| NAO6 (`maxtronics-nao6`) | Maxtronics Robotics | humanoid | duplicate / variant | `nao-6` — Aldebaran's NAO 6; Robocensus credits the Korean reseller Maxtronics, Robopear credits Aldebaran. |
| XGO-lite3 (`luwu-xgo-lite3`) | Luwu Dynamics | quadruped | duplicate / variant | `ogadjet-xgo-lite3` — Same XGO-Lite3 model; Robocensus credits Luwu Dynamics, we list the Ogadjet/XGO brand. |
| Bittle (`petoi-bittle`) | Petoi | quadruped | duplicate / variant | `petoi-bittle-x` — Original Bittle (discontinued per Robocensus); we carry Bittle X. |
| AI Sapiens (`robotis-ai-sapiens`) | ROBOTIS | humanoid | duplicate / variant | `robotis-ai-sapiens-k1` — AI Sapiens is the product line; K1 is the model we carry. |
| Go2 (`unitree-go2`) | Unitree | quadruped | duplicate / variant | `unitree-go2-pro` — Robocensus's product page (unitree.com/go2) is the same page as our Go2 Pro record; Go2 Air/Pro/EDU/W are separate records. |
| NEO (`1x-neo`) | 1X Technologies | humanoid | already carried | `1x-neo` |
| A2 (`agibot-yuanzheng-a2`) | AgiBot | humanoid | already carried | `agibot-a2` |
| A3 (`agibot-a3`) | AgiBot | humanoid | already carried | `agibot-a3` |
| X1 (`agibot-x1`) | AgiBot | humanoid | already carried | `agibot-x1` |
| X2 (`agibot-x2`) | AgiBot | humanoid | already carried | `agibot-x2` |
| Digit (`agility-robotics-digit`) | Agility Robotics | humanoid | already carried | `agility-digit-5` — Robocensus's product page is the Digit 5 page. |
| K1 (`booster-k1`) | Booster Robotics | humanoid | already carried | `booster-k1` |
| T1 (`booster-t1`) | Booster Robotics | humanoid | already carried | `booster-t1` |
| T2 (`booster-t2`) | Booster Robotics | humanoid | already carried | `booster-t2` |
| Atlas (`boston-dynamics-atlas`) | Boston Dynamics | humanoid | already carried | `boston-dynamics-atlas` — Robocensus lists the current electric Atlas; our record name says so. |
| Spot (`boston-dynamics-spot`) | Boston Dynamics | quadruped | already carried | `boston-dynamics-spot` |
| DR02 (`deep-robotics-dr02`) | DEEP Robotics | humanoid | already carried | `deep-robotics-dr02` |
| Lite 3 (`deep-robotics-lite3`) | DEEP Robotics | quadruped | already carried | `deep-robotics-lite3` |
| Lynx M20 (`deep-robotics-lynx-m20`) | DEEP Robotics | quadruped | already carried | `deep-robotics-lynx-m20` |
| X20 (`deep-robotics-x20`) | DEEP Robotics | quadruped | already carried | `deep-robotics-x20` |
| JS01 (`engineai-js01`) | EngineAI | quadruped | already carried | `engineai-js01` |
| PM01 (`engineai-pm01`) | EngineAI | humanoid | already carried | `engineai-pm01` |
| SE01 (`engineai-se01`) | EngineAI | humanoid | already carried | `engineai-se01` |
| T800 (`engineai-t800`) | EngineAI | humanoid | already carried | `engineai-t800` |
| Sprout (`fauna-sprout`) | Fauna Robotics | humanoid | already carried | `fauna-robotics-sprout` |
| Figure 03 (`figure-03`) | Figure AI | humanoid | already carried | `figure-03` |
| GR-3 (`fourier-gr3`) | Fourier Intelligence | humanoid | already carried | `fourier-gr-3` |
| N1 (`fourier-n1`) | Fourier Intelligence | humanoid | already carried | `fourier-n1` |
| ET1 (`galbot-et1`) | Galbot | humanoid | already carried | `galbot-et1` |
| Genisom L1 (`genisom-l1`) | GENISOM AI | quadruped | already carried | `genisom-gangben-l1` |
| Genisom L2 (`genisom-l2`) | GENISOM AI | quadruped | already carried | `genisom-gangben-l2` |
| Genisom M1 (`genisom-m1`) | GENISOM AI | quadruped | already carried | `genisom-tongchui-m1` — GENISOM AI's M1 is carried under its Chinese product name. |
| Vision 60 (`ghost-robotics-vision-60`) | Ghost Robotics | quadruped | already carried | `ghost-robotics-vision-60` |
| AiNex (`hiwonder-ainex`) | Hiwonder | humanoid | already carried | `hiwonder-ainex` |
| Tonybot (`hiwonder-tonybot`) | Hiwonder | humanoid | already carried | `hiwonder-tonybot` |
| Forerunner K2 (`kepler-k2`) | Kepler Robotics | humanoid | already carried | `kepler-forerunner-k2` |
| Oli (`limx-oli`) | LimX Dynamics | humanoid | already carried | `limx-cl3` |
| TRON 1 (`limx-tron1`) | LimX Dynamics | biped | already carried | `limx-dynamics-tron-1` |
| Luna (`limx-luna`) | LimX Dynamics | humanoid | already carried | `limx-luna` |
| Honey Badger 5.0 (`mab-robotics-honey-badger`) | MAB Robotics | quadruped | already carried | `mab-robotics-honey-badger-5` |
| Mini Pupper 2 (`mangdang-mini-pupper-2`) | MangDang | quadruped | already carried | `mangdang-mini-pupper-2` |
| 4NE1 (`neura-4ne1`) | Neura Robotics | humanoid | already carried | `neura-4ne1` |
| Moby (`noble-machines-moby`) | Noble Machines | humanoid | already carried | `noble-machines-moby` |
| Bittle X (`petoi-bittle-x`) | Petoi | quadruped | already carried | `petoi-bittle-x` |
| Nybble Q (`petoi-nybble-q`) | Petoi | quadruped | already carried | `petoi-nybble-q` |
| Quaddle (`petoi-quaddle`) | Petoi | quadruped | already carried | `petoi-quaddle` |
| Adam SP (`pndbotics-adam`) | PNDbotics | humanoid | already carried | `pndbotics-adam` |
| Microduck (`pollen-robotics-microduck`) | Pollen Robotics | biped | already carried | `pollen-microduck` |
| D9 (`pudu-d9`) | Pudu Robotics | humanoid | already carried | `pudu-d9` |
| RIVR ONE (`rivr-one`) | RIVR | quadruped | already carried | `rivr-one` |
| OP3 (`robotis-op3`) | ROBOTIS | humanoid | already carried | `robotis-op3` |
| Optimus (`tesla-optimus`) | Tesla | humanoid | already carried | `tesla-optimus` |
| Walker S1 (`ubtech-walker-s1`) | UBTech | humanoid | already carried | `ubtech-walker-s1` |
| Walker S2 (`ubtech-walker-s2`) | UBTech | humanoid | already carried | `ubtech-walker-s2` |
| Walker X (`ubtech-walker-x`) | UBTech | humanoid | already carried | `ubtech-walker-x` |
| A2 (`unitree-a2`) | Unitree | quadruped | already carried | `unitree-a2` |
| As2 (`unitree-as2`) | Unitree | quadruped | already carried | `unitree-as2` |
| B2 (`unitree-b2`) | Unitree | quadruped | already carried | `unitree-b2` |
| G1 (`unitree-g1`) | Unitree | humanoid | already carried | `unitree-g1` |
| H1 (`unitree-h1`) | Unitree | humanoid | already carried | `unitree-h1` |
| H2 (`unitree-h2`) | Unitree | humanoid | already carried | `unitree-h2` |
| R1 (`unitree-r1`) | Unitree | humanoid | already carried | `unitree-r1` |
| THEMIS (`westwood-robotics-themis`) | Westwood Robotics | humanoid | already carried | `westwood-robotics-themis` |
| Tiangong (`x-humanoid-tiangong`) | X-Humanoid (Beijing Humanoid Robot Innovation Center) | humanoid | already carried | `x-humanoid-tiangong` |
| CyberDog 2 (`xiaomi-cyberdog2`) | Xiaomi | quadruped | already carried | `xiaomi-cyberdog-2` |
| CyberOne (`xiaomi-cyberone`) | Xiaomi | humanoid | already carried | `xiaomi-cyberone` |
| IRON (`xpeng-iron`) | XPeng | humanoid | already carried | `xpeng-iron` |

## Robopear (241)

| Model (slug) | Maker | Catalog category | Decision | Record / reason |
|---|---|---|---|---|
| A2-W (`agibot-a2-w`) | AgiBot | wheeled_humanoid | added | `agibot-a2-w` — Wheeled version of A2, listed separately by Robopear. |
| A3 Ultra (`agibot-a3-ultra`) | AgiBot | humanoid | added | `agibot-a3-ultra` |
| G2 Max (`agibot-g2-max`) | AgiBot | wheeled_humanoid | added | `agibot-g2-max` — Listed separately from G2, the same way G1 Max sits beside AGIBOT G1. |
| Avatar (`avatar-robotics-avatar`) | Avatar Robotics | wheeled_humanoid | added | `avatar-robotics-avatar` |
| Figure 04 (`figure-04`) | Figure AI | humanoid | added | `figure-04` |
| X1 Humanoid Logistics Robot (`hangcha-x1`) | Hangcha | wheeled_humanoid | added | `hangcha-x1` |
| Lightning (`honor-lightning`) | Honor | humanoid | added | `honor-lightning` |
| Alex (`ihmc-alex`) | IHMC | humanoid | added | `ihmc-alex` |
| Jingchu 1 (`jingchu-jingchu`) | Hubei Jingchu Humanoid | humanoid | added | `jingchu-1` — The 170 cm biped of the Jingchu series; we carry Jingling and Xiaochu but not this one. |
| Kengoro (`jsk-kengoro`) | University of Tokyo JSK Laboratory | humanoid | added | `jsk-kengoro` |
| ME (`roborn-me`) | Roborn | humanoid | added | `roborn-me` |
| Synthia (`syntheva-synthia`) | Syntheva Robotics | humanoid | added | `syntheva-synthia` |
| H2 Plus (`unitree-h2-plus`) | Unitree Robotics | humanoid | added | `unitree-h2-plus` — Its own product page (unitree.com/H2plus), separate from H2. |
| Elf Xuan 2.0 (`aheadform-elf-xuan-2`) | AheadForm | upper_body_humanoid | added to Misc | `aheadform-elf-xuan-2` — Animatronic bust; no locomotion. |
| Ameca (`engineered-arts-ameca`) | Engineered Arts | upper_body_humanoid | added to Misc | `engineered-arts-ameca` — Upper body only; no locomotion. |
| Sophia (`hanson-sophia`) | Hanson Robotics | upper_body_humanoid | added to Misc | `hanson-sophia` — Upper-body social robot; no locomotion. |
| Origin (`hiro-origin`) | HIRO Industries | upper_body_humanoid | added to Misc | `hiro-origin` — Stationary dual-arm on a lift column; no locomotion. |
| NEXTAGE (`kawada-nextage`) | Kawada Robotics | upper_body_humanoid | added to Misc | `kawada-nextage` — Dual-arm upper body on a fixed base; no locomotion. |
| HELIOS (`orbit-helios`) | Orbit Robotics | upper_body_humanoid | added to Misc | `orbit-helios` — Four-armed torso; no locomotion. |
| Bimanual (`svaya-bimanual`) | Svaya Robotics | upper_body_humanoid | added to Misc | `svaya-bimanual` — Upper body only; no locomotion. |
| Punyo (`toyota-punyo`) | Toyota Research Institute | upper_body_humanoid | added to Misc | `toyota-punyo` — Soft upper-body research platform; no locomotion. |
| Alice (`aeirobot-alice`) | AeiROBOT | humanoid | duplicate / variant | `aeirobot-alice-4` — ALICE 4 is the model we carry. |
| HRP-4 (`kawada-hrp-4`) | Kawada Robotics | humanoid | duplicate / variant | `aist-hrp-4` — HRP-4 was built by Kawada for AIST; we carry it under AIST. |
| Apollo (`apptronik-apollo`) | Apptronik | humanoid | duplicate / variant | `apptronik-apollo-2` — We carry the current Apollo 2. |
| TonyPi (`hiwonder-tonypi`) | Hiwonder | humanoid | duplicate / variant | `hiwonder-tonypi-pro` — Both catalogs list the base TonyPi; we carry the current TonyPi Pro. |
| ROBOTO 01 (`roboparty-rp1`) | Shanghai RoboParty | humanoid | duplicate / variant | `roboparty-roboto-01` — RP1 is ROBOTO 01's short name; we carry it as ROBOTO 01 (RP1). |
| Motion (`vinmotion-motion`) | VinMotion | humanoid | duplicate / variant | `vinmotion-motion-1` — We carry Motion 1 and Motion 2 separately. |
| NEO (`1x-neo`) | 1X Technologies | humanoid | already carried | `1x-neo` |
| EVE (`1x-eve`) | 1X Technologies | wheeled_humanoid | already carried | `1x-technologies-eve` |
| A2 (`agibot-a2`) | AgiBot | humanoid | already carried | `agibot-a2` |
| A3 (`agibot-a3`) | AgiBot | humanoid | already carried | `agibot-a3` |
| Genie G1 (`agibot-genie-g1`) | AgiBot | wheeled_humanoid | already carried | `agibot-g1` |
| Genie G2 (`agibot-genie-g2`) | AgiBot | wheeled_humanoid | already carried | `agibot-g2` |
| RAISE A1 (`agibot-raise-a1`) | AgiBot | humanoid | already carried | `agibot-raise-a1` |
| X1 (`agibot-x1`) | AgiBot | humanoid | already carried | `agibot-x1` |
| X2 (`agibot-x2`) | AgiBot | humanoid | already carried | `agibot-x2` |
| Agile ONE (`agile-robots-agile-one`) | Agile Robots | humanoid | already carried | `agile-robots-agile-one` |
| Agile ONE SN (`agile-robots-agile-one-sn`) | Agile Robots | humanoid | already carried | `agile-robots-agile-one-sn` |
| Digit 5 (`agility-digit`) | Agility Robotics | humanoid | already carried | `agility-digit-5` |
| Digit (gen 4) (`agility-digit-gen4`) | Agility Robotics | humanoid | already carried | `agility-robotics-digit-v4` |
| AlphaBot 2 (`ai2-alphabot-2`) | AI2 Robotics | wheeled_humanoid | already carried | `ai2-robotics-alphabot-2` |
| AIDOL (`aidol-aidol`) | AIDOL Lab | humanoid | already carried | `aidol-aidol` |
| Mobo (`aimoga-mobo`) | AiMoga | humanoid | already carried | `aimoga-mobo` |
| HRP-5P (`aist-hrp-5p`) | AIST | humanoid | already carried | `aist-hrp-5p` |
| AKINCI-5 (`akinrobotics-akinci-5`) | AKINROBOTICS | humanoid | already carried | `akinrobotics-akinci-5` |
| Pepper (`aldebaran-pepper`) | Aldebaran | wheeled_humanoid | already carried | `aldebaran-pepper` |
| Abi (`andromeda-abi`) | Andromeda Robotics | humanoid | already carried | `andromeda-robotics-abi` |
| Apollo 2 (`apptronik-apollo-2`) | Apptronik | humanoid | already carried | `apptronik-apollo-2` |
| Astribot S1 (`astribot-s1`) | Astribot | wheeled_humanoid | already carried | `astribot-s1` |
| T1 (`astribot-t1`) | Astribot | humanoid | already carried | `astribot-t1` |
| Sherpa Mecha (`ati-sherpa-mecha`) | Ati Robotics | wheeled_humanoid | already carried | `ati-robotics-sherpa-mecha` |
| K1 (`booster-k1`) | Booster Robotics | humanoid | already carried | `booster-k1` |
| T1 (`booster-t1`) | Booster Robotics | humanoid | already carried | `booster-t1` |
| T2 (`booster-t2`) | Booster Robotics | humanoid | already carried | `booster-t2` |
| DexBot (`boshiac-dexbot`) | BOSHIAC | wheeled_humanoid | already carried | `boshiac-dexbot` |
| Atlas (electric) (`boston-dynamics-atlas`) | Boston Dynamics | humanoid | already carried | `boston-dynamics-atlas` — Robocensus lists the current electric Atlas; our record name says so. |
| CASBOT 02 (`casbot-02`) | CASBOT | humanoid | already carried | `casbot-02` |
| CASBOT W1 (`casbot-w1`) | CASBOT | wheeled_humanoid | already carried | `casbot-w1` |
| Clone Alpha (`clone-alpha`) | Clone Robotics | humanoid | already carried | `clone-robotics-clone-alpha-protoclone` |
| Proxie (`cobot-proxie`) | Collaborative Robotics | wheeled_humanoid | already carried | `collaborative-robotics-proxie-gen-2` |
| Alphabot G1 (`pangolin-alphabot-g1`) | Pangolin Robot | wheeled_humanoid | already carried | `csjbot-alphabot-king-g1` — Pangolin Robot is CSJBot; our record notes the English page calls it Alphabot G1. |
| Orca I (`cyan-orca`) | Cyan Robotics | humanoid | already carried | `cyan-robotics-orca` |
| Cloud Ginger XR-1 (`dataa-cloud-ginger-xr-1`) | DATAA Robotics | wheeled_humanoid | already carried | `dataa-cloud-ginger-1` — Cloud Ginger 1.0 is the same robot as XR-1; the maker's product page says so. |
| DR02 (`deep-robotics-dr02`) | DEEP Robotics | humanoid | already carried | `deep-robotics-dr02` |
| W1 Pro (`dexforce-w1-pro`) | DexForce | wheeled_humanoid | already carried | `dexforce-w1-pro` |
| Vega (`dexmate-vega`) | Dexmate | humanoid | already carried | `dexmate-vega` |
| Xialan S02 (`digit-robotics-xialan-s0`) | Digit Robotics | humanoid | already carried | `digit-robotics-xialan-s0` |
| TORO (`dlr-toro`) | DLR | humanoid | already carried | `dlr-toro` |
| Atom (`dobot-atom`) | Dobot | humanoid | already carried | `dobot-atom` |
| LUMO (`dobot-lumo`) | DOBOT | humanoid | already carried | `dobot-lumo` |
| cinnamon 1 (`donut-cinnamon-1`) | Donut Robotics | humanoid | already carried | `donut-robotics-cinnamon-1` |
| Moya (`droidup-moya`) | DroidUp | humanoid | already carried | `droidup-moya` |
| Walker 02 (`droidup-walker-02`) | DroidUp | humanoid | already carried | `droidup-xingzhe-2` — 行者二号 (Xingzhe 2) is the same robot; Robopear recorded its archived droidup.com/product/2 page. |
| DXTR (`duatic-dxtr`) | Duatic | wheeled_humanoid | already carried | `duatic-dxtr` |
| Taku (`dyna-taku`) | DYNA Robotics | wheeled_humanoid | already carried | `dyna-robotics-taku` |
| Skywalker II (`eir-skywalker-2`) | EIR Technology | humanoid | already carried | `eir-technology-skywalker-2` |
| Mirokaï (`enchanted-tools-mirokai`) | Enchanted Tools | wheeled_humanoid | already carried | `enchanted-tools-mirokai` |
| PM01 (`engineai-pm01`) | EngineAI | humanoid | already carried | `engineai-pm01` |
| SA01 (`engineai-sa01`) | EngineAI | humanoid | already carried | `engineai-sa01` |
| SE01 (`engineai-se01`) | EngineAI | humanoid | already carried | `engineai-se01` |
| T800 (`engineai-t800`) | EngineAI | humanoid | already carried | `engineai-t800` |
| Codroid 02 (`estun-codroid-codroid`) | Estun Codroid | humanoid | already carried | `estun-codroid-02` |
| Sprout (`fauna-sprout`) | Fauna Robotics | humanoid | already carried | `fauna-robotics-sprout` |
| Figure 01 (`figure-01`) | Figure AI | humanoid | already carried | `figure-01` |
| Figure 02 (`figure-02`) | Figure AI | humanoid | already carried | `figure-02` |
| Figure 03 (`figure-03`) | Figure AI | humanoid | already carried | `figure-03` |
| Phantom (`foundation-phantom-mk-1`) | Foundation Robotics | humanoid | already carried | `foundation-phantom-mk1` |
| GR-1 (`fourier-gr-1`) | Fourier | humanoid | already carried | `fourier-gr-1` |
| GR-3 (`fourier-gr-3`) | Fourier | humanoid | already carried | `fourier-gr-3` |
| GR-2 (`fourier-gr-2`) | Fourier | humanoid | already carried | `fourier-intelligence-gr-2` |
| N1 (`fourier-n1`) | Fourier | humanoid | already carried | `fourier-n1` |
| Futuring F2 (`futuring-2`) | Futuring Robot | wheeled_humanoid | already carried | `futuring-f2` |
| Kengo (`galaxea-kengo`) | Galaxea | humanoid | already carried | `galaxea-kengo` |
| Nexo (`galaxea-nexo`) | Galaxea | wheeled_humanoid | already carried | `galaxea-nexo` |
| Galaxea R1 (`galaxea-r1`) | Galaxea AI | wheeled_humanoid | already carried | `galaxea-r1` |
| ET1 (`galbot-et1`) | Galbot | humanoid | already carried | `galbot-et1` |
| Galbot G1 (`galbot-g1`) | Galbot | wheeled_humanoid | already carried | `galbot-g1` |
| Galbot S1 (`galbot-s1`) | Galbot | wheeled_humanoid | already carried | `galbot-s1` |
| Gino 1 (`geekplus-gino-1`) | Geek+ | wheeled_humanoid | already carried | `geekplus-gino-1` |
| GENE.01 (`generative-bionics-gene-01`) | Generative Bionics | humanoid | already carried | `generative-bionics-gene-01` |
| NE01 (`genisom-ne01`) | GENISOM AI | humanoid | already carried | `genisom-yinyi-ne01` |
| Luna (`gento-luna`) | Gento Robotics | wheeled_humanoid | already carried | `gento-robotics-gento-luna` |
| Maker H01 (`gigaai-maker-h01`) | GigaAI | wheeled_humanoid | already carried | `gigaai-maker-h01` |
| Laborer C1 (`glroad-laborer-c1`) | Glroad | humanoid | already carried | `glroad-laborer-c1` |
| Laborer M1 (`glroad-laborer-m1`) | Glroad | humanoid | already carried | `glroad-laborer-m1` |
| AEON (`hexagon-aeon`) | Hexagon | wheeled_humanoid | already carried | `hexagon-aeon` |
| AiNex (`hiwonder-ainex`) | Hiwonder | humanoid | already carried | `hiwonder-ainex` |
| Tonybot (`hiwonder-tonybot`) | Hiwonder | humanoid | already carried | `hiwonder-tonybot` |
| ASIMO (`honda-asimo`) | Honda | humanoid | already carried | `honda-asimo` |
| HSR-ER-HR705 (`huashu-hr705`) | Huashu Robot | wheeled_humanoid | already carried | `huashu-hsr-er-hr705` |
| HMND 01 Alpha Bipedal (`humanoid-hmnd-01-biped`) | Humanoid | humanoid | already carried | `humanoid-hmnd-01-alpha` — Our record covers HMND 01 Alpha (the wheeled page); the bipedal Alpha shares it. |
| HMND 01 Alpha Wheeled (`humanoid-hmnd-01-wheeled`) | Humanoid | wheeled_humanoid | already carried | `humanoid-hmnd-01-alpha` |
| TARA GEN1 (`ihub-tara-gen1`) | iHub Robotics | wheeled_humanoid | already carried | `ihub-robotics-tara-gen-1` |
| pib.Pro (`isento-pib-pro`) | isento robotics | upper_body_humanoid | already carried | `isento-pib-pro` |
| JAKA Kargo (`jaka-kargo`) | JAKA Robotics | wheeled_humanoid | already carried | `jaka-kargo` |
| JAKA π (`jaka-pi`) | JAKA Robotics | humanoid | already carried | `jaka-pi` |
| Jingchu Elf (`jingchu-elf`) | Hubei Jingchu Humanoid | wheeled_humanoid | already carried | `jingchu-jingling` — Jingchu Elf (荆楚精灵) is Jingling. |
| RayNex G3 (`nineray-raynex-g3`) | NineRay | humanoid | already carried | `jiuguang-raynex-g3` |
| K-Bot (`kscale-kbot`) | K-Scale Labs | humanoid | already carried | `k-scale-labs-k-bot` |
| RHP Kaleido (`kawasaki-kaleido`) | Kawasaki Heavy Industries | humanoid | already carried | `kawasaki-kaleido-9` |
| XMAN-F1 (`keenon-xman-f1`) | KEENON Robotics | humanoid | already carried | `keenon-xman-f1` |
| XMAN-R1 (`keenon-xman-r1`) | KEENON Robotics | wheeled_humanoid | already carried | `keenon-xman-r1` |
| Forerunner K1 (`kepler-k1`) | Kepler | humanoid | already carried | `kepler-forerunner-k1` |
| Forerunner K2 (`kepler-k2`) | Kepler | humanoid | already carried | `kepler-forerunner-k2` |
| KAI Bot (`kinetixai-kai`) | KinetixAI | humanoid | already carried | `kinetix-ai-kaibot` |
| ARMAR-6 (`kit-armar-6`) | KIT H2T | wheeled_humanoid | already carried | `kit-armar-6` |
| ARMAR-7 (`kit-armar-7`) | KIT H2T | wheeled_humanoid | already carried | `kit-armar-7` |
| Knowin-X1 (`knowin-x1`) | Knowin | wheeled_humanoid | already carried | `knowin-ai-knowin-x1` |
| VB1 (`lanxin-versabot-vb-1`) | Lanxin Robotics | wheeled_humanoid | already carried | `lanxin-vb1` |
| VB1-I (`lanxin-vb1-i`) | Lanxin Robotics | wheeled_humanoid | already carried | `lanxin-vb1-i` |
| VB2 (`lanxin-vb2`) | Lanxin Robotics | wheeled_humanoid | already carried | `lanxin-vb2` |
| Kuavo 4 Pro (`leju-kuavo-4-pro`) | Leju Robotics | humanoid | already carried | `leju-kuavo-4-pro` |
| Kuavo 5 (`leju-kuavo-5`) | Leju Robotics | humanoid | already carried | `leju-kuavo-5` |
| CLOiD (`lg-cloid`) | LG Electronics | wheeled_humanoid | already carried | `lg-cloid` |
| Lightbot 0 (`light-origins-lightbot-0`) | Light Origins | humanoid | already carried | `light-origins-lightbot-0` |
| Lumi (`lightberry-lumi`) | Lightberry | humanoid | already carried | `lightberry-lumi` |
| CL-1 (`limx-cl-1`) | LimX Dynamics | humanoid | already carried | `limx-cl-1` |
| Oli (`limx-oli`) | LimX Dynamics | humanoid | already carried | `limx-cl3` |
| TRON 1 (`limx-tron-1`) | LimX Dynamics | legged_platform | already carried | `limx-dynamics-tron-1` |
| Luna (`limx-luna`) | LimX Dynamics | humanoid | already carried | `limx-luna` |
| TRON 2 (`limx-tron-2`) | LimX Dynamics | humanoid | already carried | `limx-tron-2` |
| LUS2 (`lumos-lus2`) | Lumos Robotics | humanoid | already carried | `lumos-robotics-lus2` |
| NIX S3 (`lumos-nix`) | Lumos Robotics | humanoid | already carried | `lumos-robotics-nix` |
| MagicBot Gen1 (`magiclab-magicbot-gen1`) | MagicLab | humanoid | already carried | `magiclab-magicbot-gen1` |
| MagicBot Z1 (`magiclab-magicbot-z1`) | MagicLab | humanoid | already carried | `magiclab-z1` |
| MATRIX-1 (`matrix-matrix-1`) | Matrix Robotics | humanoid | already carried | `matrix-robotics-matrix-1` |
| MATRIX-3 (`matrix-matrix-3`) | Matrix Robotics | humanoid | already carried | `matrix-robotics-matrix-3` |
| Asimov 1 (`menloai-asimov-1`) | MenloAI | humanoid | already carried | `menlo-research-asimov-v1` |
| MenteeBot V3 (`mentee-menteebot`) | Mentee Robotics | humanoid | already carried | `mentee-menteebot` |
| Max (`meta-max`) | Meta | humanoid | already carried | `meta-max` |
| MIRO U (`midea-miro-u`) | Midea | wheeled_humanoid | already carried | `midea-miro-u` |
| Bolt (`mirrorme-bolt`) | MirrorMe Technology | humanoid | already carried | `mirrorme-bolt` |
| MH3 (`mirsee-mh3`) | Mirsee Robotics | wheeled_humanoid | already carried | `mirsee-robotics-mh3` |
| Spaceo M1 (`muks-spaceo-m1`) | Muks Robotics | wheeled_humanoid | already carried | `muks-spaceo-m1` |
| Spaceo PRO (`muks-spaceo-pro`) | Muks Robotics | wheeled_humanoid | already carried | `muks-spaceo-pro` |
| NAO6 (`aldebaran-nao`) | Aldebaran | humanoid | already carried | `nao-6` |
| Neo1 (`neodra-neo1`) | Neodra Dynamics | humanoid | already carried | `neodradynamics-neo1` |
| Billi (`neubility-billi`) | Neubility | wheeled_humanoid | already carried | `neubility-billi` |
| 4NE1 (`neura-4ne-1`) | NEURA Robotics | humanoid | already carried | `neura-4ne1` |
| 4NE1 Mini (`neura-4ne-1-mini`) | NEURA Robotics | humanoid | already carried | `neura-4ne1-mini` |
| Moby (`noble-moby`) | Noble Machines | humanoid | already carried | `noble-machines-moby` |
| Bumi (`noetix-bumi`) | Noetix Robotics | humanoid | already carried | `noetix-bumi` |
| E1 (`noetix-e1`) | Noetix Robotics | humanoid | already carried | `noetix-e1` |
| N2 (`noetix-n2`) | Noetix Robotics | humanoid | already carried | `noetix-n2` |
| W1 (`noetix-w1`) | Noetix Robotics | wheeled_humanoid | already carried | `noetix-w1` |
| Xiao Nuo (`noetix-xiao-nuo`) | Noetix Robotics | upper_body_humanoid | already carried | `noetix-xiaonuo` — Carried in Misc: fixed robotic head, no locomotion. |
| Modular (`o-id-modular`) | O-ID | humanoid | already carried | `o-id-modular` |
| RoBee (`oversonic-robee`) | Oversonic Robotics | wheeled_humanoid | already carried | `oversonic-robee` |
| ARI (`pal-ari`) | PAL Robotics | wheeled_humanoid | already carried | `pal-ari` |
| Kangaroo (`pal-kangaroo`) | PAL Robotics | humanoid | already carried | `pal-kangaroo` |
| REEM-C (`pal-reem-c`) | PAL Robotics | humanoid | already carried | `pal-reemc` |
| TALOS (`pal-talos`) | PAL Robotics | humanoid | already carried | `pal-talos` |
| TORA DOUBLE ONE (`paxini-tora-doubleone`) | PaXini | wheeled_humanoid | already carried | `paxini-tora-double-one` |
| PR-OMNI (`perceptyne-pr-omni`) | Perceptyne | wheeled_humanoid | already carried | `perceptyne-pr-omni` |
| Persona Gen 1 (`persona-ai-gen1`) | Persona AI | humanoid | already carried | `persona-ai-gen-1` |
| PHYBOT C1 (`phybot-c1`) | PHYBOT | humanoid | already carried | `phybot-c1` |
| M1 (`phybot-m1`) | Phybot | humanoid | already carried | `phybot-m1` |
| Adam (`pndbotics-adam`) | PNDbotics | humanoid | already carried | `pndbotics-adam` |
| Reachy 2 (`pollen-reachy-2`) | Pollen Robotics | wheeled_humanoid | already carried | `pollen-reachy-2` |
| PrimeBOT T1 (`primebot-t1`) | PrimeBOT | wheeled_humanoid | already carried | `primebot-t1` |
| Promobot V.4 (`promobot-v4`) | Promobot | wheeled_humanoid | already carried | `promobot-v4` |
| D9 (`pudu-d9`) | Pudu Robotics | humanoid | already carried | `pudu-d9` |
| PrimeBOT Q1 (`primebot-q1`) | PrimeBOT | humanoid | already carried | `qiyuan-primebot-q1` |
| RB-Y1 (`rainbow-rb-y1`) | Rainbow Robotics | wheeled_humanoid | already carried | `rainbow-rby1` |
| RealBot-01 (`realman-realbot-01`) | RealMan Robotics | wheeled_humanoid | already carried | `realman-realbot-01` |
| RealBot-L2 (`realman-realbot-l2`) | RealMan Robotics | wheeled_humanoid | already carried | `realman-realbot-l2` |
| RealBot-S2 (`realman-realbot-s2`) | RealMan Robotics | wheeled_humanoid | already carried | `realman-realbot-s2` |
| Reflex (`reflex-robotics-reflex`) | Reflex Robotics | wheeled_humanoid | already carried | `reflex-robotics-reflex` |
| Dex (`richtech-dex`) | Richtech Robotics | wheeled_humanoid | already carried | `richtech-dex` |
| Robbyant R1 (`robbyant-r1`) | Robbyant | wheeled_humanoid | already carried | `robbyant-r1` |
| ROBO-T1 (`robo-robo-t1`) | Robo Robotics | humanoid | already carried | `robo-robotics-robo-t1` |
| TITAN (`roboforce-titan`) | RoboForce | wheeled_humanoid | already carried | `roboforce-titan` |
| ROBOTO Origin (`roboparty-roboto-origin`) | Shanghai RoboParty | humanoid | already carried | `roboparty-roboto-origin` |
| REX G1 (`roboscience-rex-g1`) | RoboScience | wheeled_humanoid | already carried | `roboscience-rex-g1` |
| RNoid (`robot-com-rnoid`) | Robot.com | wheeled_humanoid | already carried | `robot-com-r-noid` |
| L7 (`robotera-l7`) | RobotEra | humanoid | already carried | `robotera-l7` |
| Q5 (`robotera-q5`) | RobotEra | wheeled_humanoid | already carried | `robotera-q5` |
| AI Worker (`robotis-ai-worker`) | ROBOTIS | wheeled_humanoid | already carried | `robotis-ai-worker` |
| ROBOTIS OP3 (`robotis-op3`) | ROBOTIS | humanoid | already carried | `robotis-op3` |
| Phoenix (`sanctuary-phoenix`) | Sanctuary AI | humanoid | already carried | `sanctuary-phoenix` |
| D01 (`sharpa-d01`) | Sharpa | wheeled_humanoid | already carried | `sharpa-d01` |
| North (`sharpa-north`) | Sharpa | wheeled_humanoid | already carried | `sharpa-north` |
| Moz1 (`spirit-ai-moz1`) | Spirit AI | wheeled_humanoid | already carried | `spirit-ai-moz1` |
| Memo (`sunday-memo`) | Sunday Robotics | wheeled_humanoid | already carried | `sunday-robotics-memo` |
| Onero H1 (`switchbot-onero-h1`) | SwitchBot | wheeled_humanoid | already carried | `switchbot-onero-h1` |
| Optimus (`tesla-optimus`) | Tesla | humanoid | already carried | `tesla-optimus` |
| T1 (`tlibot-t1`) | Tlibot | humanoid | already carried | `tianlian-t1` — TLibot is Sichuan Tianlian's brand. |
| Tianzhen Z1 (`tlibot-tianzhen-z1`) | Tlibot | humanoid | already carried | `tianlian-tianzhen-z1` — TLibot is Sichuan Tianlian's brand. |
| Y1 (`tlibot-y1`) | Tlibot | wheeled_humanoid | already carried | `tianlian-y1` — TLibot is Sichuan Tianlian's brand. |
| Walker Tienkung (`ubtech-tiangong-xingzhe`) | UBTECH Robotics | humanoid | already carried | `tien-kung-xingzhe` |
| Star (`topstar-star`) | Topstar | humanoid | already carried | `topstar-star` |
| TWH020 (`topstar-twh020`) | Topstar | wheeled_humanoid | already carried | `topstar-twh020` |
| T-HR3 (`toyota-t-hr3`) | Toyota Motor Corporation | humanoid | already carried | `toyota-t-hr3` |
| Voxel (`tuesday-labs-voxel`) | Tuesday Labs | humanoid | already carried | `tuesday-labs-voxel-series-1` |
| Alpha Mini (`ubtech-alpha-mini`) | UBTECH Robotics | humanoid | already carried | `ubtech-alpha-mini` |
| Cruzr S2 (`ubtech-cruzr-s2`) | UBTECH | wheeled_humanoid | already carried | `ubtech-cruzr-s2` |
| UWORLD U1 (`ubtech-uworld-u1`) | UBTECH Robotics | humanoid | already carried | `ubtech-uworld-u1` |
| Walker C1 (`ubtech-walker-c1`) | UBTECH | humanoid | already carried | `ubtech-walker-c1` |
| Walker S1 (`ubtech-walker-s1`) | UBTECH Robotics | humanoid | already carried | `ubtech-walker-s1` |
| Walker S2 (`ubtech-walker-s2`) | UBTECH Robotics | humanoid | already carried | `ubtech-walker-s2` |
| Walker X (`ubtech-walker-x`) | UBTECH Robotics | humanoid | already carried | `ubtech-walker-x` |
| Yanshee (`ubtech-yanshee`) | UBTECH Robotics | humanoid | already carried | `ubtech-yanshee` |
| G1 (`unitree-g1`) | Unitree Robotics | humanoid | already carried | `unitree-g1` |
| G1+ (`unitree-g1-plus`) | Unitree Robotics | humanoid | already carried | `unitree-g1` |
| H1 (`unitree-h1`) | Unitree Robotics | humanoid | already carried | `unitree-h1` |
| H2 (`unitree-h2`) | Unitree Robotics | humanoid | already carried | `unitree-h2` |
| R1 (`unitree-r1`) | Unitree Robotics | humanoid | already carried | `unitree-r1` |
| Superman (`unitree-superman`) | Unitree Robotics | humanoid | already carried | `unitree-superman` |
| Wanda 2.0 (`unix-wanda`) | UniX AI | wheeled_humanoid | already carried | `unix-ai-wanda-2` |
| Calvin-40 (`wandercraft-calvin`) | Wandercraft | humanoid | already carried | `wandercraft-calvin-40` |
| Isaac (`weave-isaac`) | Weave Robotics | wheeled_humanoid | already carried | `weave-isaac-1` |
| Allex (`wirobotics-allex`) | Wirobotics | humanoid | already carried | `wirobotics-allex` |
| Tiangong 3.0 (`x-humanoid-tiangong-3`) | X-Humanoid | humanoid | already carried | `x-humanoid-tiangong-3` |
| Tiangong Ultra (`x-humanoid-tiangong-ultra`) | X-Humanoid | humanoid | already carried | `x-humanoid-tiangong-ultra` |
| Quanta X2 (`x-square-quanta-x2`) | X Square Robot | wheeled_humanoid | already carried | `x-square-robot-quanta-x2` |
| CyberOne (`xiaomi-cyberone`) | Xiaomi | humanoid | already carried | `xiaomi-cyberone` |
| IRON (`xpeng-iron`) | XPENG | humanoid | already carried | `xpeng-iron` |
| W-Bot 2.0 (`yuequan-w-bot`) | Yue Quan Bionics | wheeled_humanoid | already carried | `yue-quan-bionics-w-bot` |
| X-Bot (`yuequan-x-bot`) | Yue Quan Bionics | humanoid | already carried | `yue-quan-bionics-x-bot` |
| Jupiter (`zeroth-jupiter`) | Zeroth Robotics | humanoid | already carried | `zeroth-jupiter` |
| F-Series (`realbotix-f-series`) | Realbotix | wheeled_humanoid | out of scope | Companion/display robot in the owner's excluded class (companion robots). |

## New records

| id | Name | Maker | Category | Locomotion | `official_url` | `seen_on` |
|---|---|---|---|---|---|---|
| `agibot-a2-w` | A2-W | AgiBot | Humanoid | Wheeled | https://www.agibot.com/products/A2W | https://robopear.com/robots/agibot-a2-w |
| `agibot-a3-ultra` | A3 Ultra | AgiBot | Humanoid | Legged | https://www.agibot.com/products/A3Ultra | https://robopear.com/robots/agibot-a3-ultra |
| `agibot-g2-max` | G2 Max | AgiBot | Humanoid | Wheeled | https://www.agibot.com/products/G2Max | https://robopear.com/robots/agibot-g2-max |
| `aheadform-elf-xuan-2` | Elf Xuan 2.0 | AheadForm | Misc |  | https://www.aheadform.com/elf-xuan-2/ | https://robopear.com/robots/aheadform-elf-xuan-2 |
| `avatar-robotics-avatar` | Avatar | Avatar Robotics | Humanoid | Wheeled | https://www.avatarrobotics.com/platform | https://robopear.com/robots/avatar-robotics-avatar |
| `engineered-arts-ameca` | Ameca | Engineered Arts | Misc |  | https://engineeredarts.com/robots/ameca | https://robopear.com/robots/engineered-arts-ameca |
| `figure-04` | Figure 04 | Figure AI | Humanoid |  | — (none found) | https://robopear.com/robots/figure-04 |
| `hangcha-x1` | X1 Humanoid Logistics Robot | Hangcha | Humanoid | Wheeled | https://www.hcforklift.com/talk/detail/470 | https://robopear.com/robots/hangcha-x1 |
| `hanson-sophia` | Sophia | Hanson Robotics | Misc |  | https://www.hansonrobotics.com/sophia-utility | https://robopear.com/robots/hanson-sophia |
| `hiro-origin` | Origin | HIRO Industries | Misc |  | https://www.hiroindustries.com/ | https://robopear.com/robots/hiro-origin |
| `hiwonder-mechdog` | MechDog | Hiwonder | Quadruped | Legged | https://www.hiwonder.com/products/mechdog | https://robocensus.com/robots/hiwonder-mechdog/ |
| `hiwonder-puppypi` | PuppyPi | Hiwonder | Quadruped | Legged | https://www.hiwonder.com/products/puppypi | https://robocensus.com/robots/hiwonder-puppypi/ |
| `hiwonder-rospug` | ROSPug | Hiwonder | Quadruped | Legged | https://www.hiwonder.com/products/rospug | https://robocensus.com/robots/hiwonder-rospug/ |
| `honor-lightning` | Lightning | HONOR | Humanoid | Legged | — (none found) | https://robopear.com/robots/honor-lightning |
| `ihmc-alex` | Alex | IHMC | Humanoid | Legged | https://robots.ihmc.us/alex-humanoid | https://robopear.com/robots/ihmc-alex |
| `jingchu-1` | Jingchu 1 (荆楚一号) | Hubei Jingchu Humanoid Robot (JCBOT) | Humanoid | Legged | https://www.jingchurobot.cn/product_detail/1.html | https://robopear.com/robots/jingchu-jingchu |
| `jsk-kengoro` | Kengoro | University of Tokyo JSK Laboratory | Humanoid | Legged | https://www.jsk.t.u-tokyo.ac.jp/research/kengoro.html | https://robopear.com/robots/jsk-kengoro |
| `kawada-nextage` | NEXTAGE | Kawada Robotics | Misc |  | https://www.kawadarobot.co.jp/en/nextage/ | https://robopear.com/robots/kawada-nextage |
| `mangdang-mini-pupper-1` | Mini Pupper (1st generation) | MangDang | Quadruped | Legged | https://mangdang.store/products/mini-pupper | https://robocensus.com/robots/mangdang-mini-pupper-1/ |
| `orbit-helios` | HELIOS | Orbit Robotics | Misc |  | https://www.orbitrobotics.ch/ | https://robopear.com/robots/orbit-helios |
| `roborn-me` | ME | Roborn | Humanoid |  | https://www.roborn.com/?page_id=961 | https://robopear.com/robots/roborn-me |
| `svaya-bimanual` | Bimanual | Svaya Robotics | Misc |  | https://svayarobotics.com/product/ | https://robopear.com/robots/svaya-bimanual |
| `syntheva-synthia` | Synthia | Syntheva Robotics | Humanoid | Legged | https://robotics.syntheva.no/products/synthia | https://robopear.com/robots/syntheva-synthia |
| `tny-robotics-tny-360` | TNY-360 | TNY Robotics | Quadruped | Legged | https://tny-robotics.com/tny-360 | https://robocensus.com/robots/tny-robotics-tny-360/ |
| `toyota-punyo` | Punyo | Toyota Research Institute | Misc |  | https://punyo.tech/ | https://robopear.com/robots/toyota-punyo |
| `unitree-h2-plus` | H2 Plus | Unitree Robotics | Humanoid | Legged | https://www.unitree.com/H2plus | https://robopear.com/robots/unitree-h2-plus |

