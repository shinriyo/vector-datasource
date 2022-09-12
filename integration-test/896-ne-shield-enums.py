# -*- encoding: utf-8 -*-
import unittest

import dsl
from shapely.wkt import loads as wkt_loads

from . import BROKEN
from . import FixtureTest


class NeShieldEnums(FixtureTest):

    def setUp(self):
        super(NeShieldEnums, self).setUp()
        self.generate_fixtures(dsl.way(1, wkt_loads('LINESTRING (-81.10940459837249 34.03599053509704, -81.17713178350343 33.99952205079575, -81.23964918516275 33.95437059404181, -81.33168869316121 33.91095573177837, -81.38031333889623 33.87622384196766, -81.47061625240411 33.79460390091243, -81.51924089813917 33.75813541661115, -81.63732932349568 33.67998866453699, -81.72936883149413 33.64004699125464, -81.80751558356829 33.62615423533035, -81.93602357586801 33.56537342816159, -81.94991633179229 33.5497440777467, -82.01243373345163 33.52890494386028)'), {u'labelrank': 0, u'length_km': 112, u'scalerank': 4, u'min_zoom': 4, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'USA', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 1, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 177505, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'20', u'level': u'Interstate', u'type': u'Major Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(2, wkt_loads('LINESTRING (-102.624073741633 22.86274158298323, -102.2402863592243 23.39240290259696)'), {u'labelrank': 0, u'length_km': 69, u'scalerank': 7, u'min_zoom': 7, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'MEX', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 253705, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'54', u'level': u'Federal', u'type': u'Secondary Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(3, wkt_loads('LINESTRING (-102.624073741633 22.86274158298323, -102.7473719504611 23.00340573671671, -102.7977331906867 23.09197205573405, -102.8394114584596 23.20311410312845, -102.8984556711378 23.23089961497701)'), {u'labelrank': 0, u'length_km': 50, u'scalerank': 4, u'min_zoom': 4, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'MEX', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 1, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 253805, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'49', u'level': u'Interstate', u'type': u'Secondary Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(4, wkt_loads('LINESTRING (-121.4227091016939 49.37532967000865, -121.4435482355804 49.36143691408435, -121.5303779601072 49.35622713061275, -121.5824757948233 49.34580756366951, -121.6189442791246 49.32323183529254, -121.6675689248596 49.26245102812376, -121.6710421138407 49.21903616586031, -121.6866714642555 49.20688000442659, -121.7266131375379 49.19646043748334, -121.8064964841026 49.1547821697105, -121.9124287480253 49.1547821697105, -122.0565660907398 49.13567963031458, -122.0999809530033 49.12178687439028, -122.1069273309654 49.09747455152276, -122.1416592207762 49.08358179559848, -122.1711813271153 49.05926947273096, -122.2076498114166 49.04537671680665, -122.2458548902084 49.04016693333502, -122.325738236773 49.04884990578773, -122.3882556384324 49.06968903967417, -122.442090067639 49.09573795703222, -122.5237100086943 49.12352346888081, -122.7859357767653 49.1929872485023, -122.8137212886139 49.21903616586031, -122.8484531784246 49.23292892178466, -122.9526488478569 49.25376805567108, -123.0186394384973 49.25724124465212, -123.0377419778932 49.31281226834934, -123.0620543007607 49.32844161876416, -123.1054691630241 49.33886118570738, -123.1311988635117 49.34147144517711)'), {u'labelrank': 0, u'length_km': 203, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'CAN', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 1, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 391905, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'1', u'level': u'Interstate', u'type': u'Major Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(5, wkt_loads('LINESTRING (-123.1311988635117 49.34147144517711, -123.2252941828711 49.35101734714114, -123.2582894781914 49.35970031959379, -123.2791286120778 49.37011988653703)'), {u'labelrank': 0, u'length_km': 17, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'', u'continent': u'North America', u'namealtt': u'State', u'localalt': u'', u'question': 0, u'sov_a3': u'CAN', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 1, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'99', u'uident': 391905, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'1', u'level': u'Interstate', u'type': u'Major Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(6, wkt_loads('LINESTRING (-4.127521700017609 51.69313357342941, -4.118856071223563 51.68788052817255, -4.109596886233094 51.68477128539421, -4.099853522723682 51.68310291122048, -4.081693911524863 51.68179329582886, -3.952886383423927 51.69231105329479, -3.933484241808992 51.69185020868032, -3.914249812632858 51.68967432208313, -3.895241430656847 51.68528463129383, -3.886250585568455 51.68130911730989, -3.878808528393088 51.6756477287238, -3.86036599360188 51.65367010739664, -3.853033314103996 51.6475507909342, -3.844934990863779 51.64243774910452, -3.836419574080149 51.63822306259918, -3.827134138447084 51.63462964130191, -3.785035399571715 51.62215183585562, -3.771991746940626 51.6167237863148, -3.75954602561309 51.61012904154762, -3.748064286216334 51.60229176636434, -3.73377372806205 51.58929478154231, -3.721256546651884 51.57411607664692, -3.710942960850564 51.55738275036239, -3.700320200814235 51.53286465017969, -3.696423438758081 51.52729368047365, -3.691217061310308 51.52299440856441, -3.684335017843615 51.51996683445194, -3.675231878339689 51.51846471434794, -3.666372286464245 51.51919098212637, -3.65767894865858 51.52155062322177, -3.621291182916416 51.53765976756021, -3.611699489786418 51.54104901719285, -3.600710679122837 51.54320448662364, -3.5892872744874 51.5436944986187, -3.56666651241665 51.54172570042416, -3.544842019837928 51.5374351787291, -3.460662042515579 51.50886281263474, -3.439247351635117 51.50356601630691, -3.417478277079637 51.50009218127033, -3.395208981945853 51.49861047833277, -3.347836780647186 51.50087386707199, -3.301036260009452 51.50864697401784, -3.2567514259536 51.52076602068203, -3.214592893947886 51.53667682683196, -3.191353783407142 51.5419036214462, -3.098398799613265 51.5483000280249, -3.087706037863383 51.55056633350212, -3.077494537894366 51.55429100801244, -3.069823516780824 51.55853194516039, -3.034831410203219 51.58343505476773, -3.020728981654176 51.59068606559978, -3.005741323102137 51.59550743362284, -2.989315712683533 51.5974120635799, -2.950345175383938 51.59667121211118)'), {u'labelrank': 5, u'length_km': 136, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'E', u'continent': u'Europe', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'E30', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 1, u'local': u'M4', u'edited': u'New in version 2.0.0', u'label2': u'M4', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'30', u'level': u'E', u'type': u'Major Highway', u'routeraw': u'E30 M4', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(7, wkt_loads('LINESTRING (-2.950345175383938 51.59667121211118, -2.884015635025397 51.59836292018945, -2.860955903875714 51.60172591917951, -2.849300618564051 51.60243176979149, -2.837849504916994 51.60116882220894, -2.82654131143517 51.59725747646245, -2.795184918856821 51.57947704121221, -2.782905451599037 51.57444566804838, -2.720143081895175 51.55907737517872, -2.708763428330747 51.55432309213116, -2.698785267407007 51.5474425070335, -2.692747619610429 51.54055900519778, -2.688261676464954 51.53269256263381, -2.685024097211699 51.524169854005, -2.679400626220485 51.4974000320354)'), {u'labelrank': 7, u'length_km': 33, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'E', u'continent': u'Europe', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'E30', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 1, u'local': u'M4', u'edited': u'New in version 2.0.0', u'label2': u'M4', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'30', u'level': u'E', u'type': u'Major Highway', u'routeraw': u'E30 M4', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(8, wkt_loads('LINESTRING (-2.58760942091494 51.54348449347795, -2.568163528229022 51.52722659549817, -2.546850923180887 51.51297249656971, -2.523745982591195 51.50218348246363, -2.498936208601934 51.49632375568905, -2.460384223214779 51.49401661587887, -2.441084167432171 51.49479538494248, -2.280154603010556 51.51910931346052, -2.096006345214662 51.51882055639201, -2.067292517324067 51.52216605495369, -2.040744367447488 51.52780410963518, -1.956105003879741 51.55562687404665, -1.931159601570402 51.56039865752257, -1.905702311730501 51.5609645047074, -1.892945957798929 51.55874778377724, -1.855757547457634 51.54715666670303, -1.718896905556492 51.53166295409653, -1.689758692277325 51.52611240155698, -1.482842377138343 51.46746554926421, -1.431596747688039 51.45985577965004, -1.379665684792241 51.45732988448493, -1.354957996635282 51.45924618139427, -1.350399135038151 51.46004245088628, -1.337348190561906 51.46475589960091, -1.328201299986971 51.46707762310145, -1.318608148487973 51.46788847628378, -1.299194339920778 51.46797014494965)'), {
                               u'labelrank': 4, u'length_km': 145, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'E', u'continent': u'Europe', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'E30', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 1, u'local': u'M4', u'edited': u'New in version 2.0.0', u'label2': u'M4', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'30', u'level': u'E', u'type': u'Major Highway', u'routeraw': u'E30 M4', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(9, wkt_loads('LINESTRING (-1.299194339920778 51.46797014494965, -1.155164355853451 51.45538150345685, -1.130417291732613 51.44752381110708, -1.077385160216905 51.4248228387395, -1.049361140878933 51.41610762539835, -1.029979416430463 51.41228378179387, -1.010341019032198 51.41009331150632, -0.9903701134944061 51.40941079479889, -0.971110892044704 51.41074374409503, -0.9519697984866916 51.41421757913159, -0.9146997194795335 51.42489867392926, -0.7910300254818186 51.48171381471656, -0.7715520486771754 51.48809563760493, -0.7513040530231239 51.49241824341873, -0.6493217649150269 51.49868048004636, -0.5261231241149692 51.4942207875435)'), {u'labelrank': 6, u'length_km': 87, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'E', u'continent': u'Europe', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'E30', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 1, u'local': u'M4', u'edited': u'New in version 2.0.0', u'label2': u'M4', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'30', u'level': u'E', u'type': u'Major Highway', u'routeraw': u'E30 M4', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(10, wkt_loads('LINESTRING (30.36037628818696 40.69652363282226, 30.25813086543583 40.69218344600442, 30.20183782076233 40.69801692213638, 30.14676397260042 40.71113057648102, 30.09802527951785 40.72798348902625, 30.00932144145514 40.77122121411643, 29.98738173772281 40.7796797545078, 29.96441534219124 40.78498238431172, 29.93844470645173 40.78698910010114, 29.83220543913633 40.7809981201136, 29.5274588125262 40.78741494385876, 29.51620020359148 40.78927582274488, 29.50511659894075 40.79193588786104, 29.49431883462046 40.79554680958672, 29.48313606087549 40.80078527115325, 29.4725891360289 40.80721376185067, 29.36037055567824 40.89534591925241, 29.32207961834801 40.93078428675411, 29.31344607367269 40.93753361863883, 29.30529670751633 40.94146538155179, 29.29648232508092 40.94324459177204, 29.27834021431052 40.9449304663742, 29.23974593622141 40.95320816900545, 29.22112548040816 40.95977082965388, 29.20350838248963 40.96857937861316, 29.20059747789978 40.97053942659351, 29.19306646021342 40.9772012563362, 29.18888385782676 40.98039800125653, 29.18435708034836 40.98297639770686, 29.17953862906336 40.98498311349626, 29.17448683873307 40.98647064990988, 29.1467544932017 40.99142327114594, 29.13809178114573 40.99505169330003, 29.12318724962855 41.00971705229581, 29.11435536676476 41.0292766977663, 29.1078102065447 41.05041721526852, 29.09976000948257 41.06982519035958, 29.0889797455907 41.08542390553649, 29.07584859081764 41.09866589635602, 29.06042487992472 41.10900281606188, 29.04278444810164 41.11589215137376, 29.03367839185965 41.11790470063929, 29.01513377123611 41.12001641899904, 28.9715752049587 41.11953807395622, 28.9602582612627 41.1181847074936, 28.94471788084712 41.11450378405433, 28.9306067020839 41.10867614139848, 28.91737637821658 41.10098761985655, 28.87865376365258 41.07417696355402, 28.8647292561256 41.06733429605125, 28.84987139241746 41.06251001129012, 28.81550638452405 41.05633819354251, 28.75161232045061 41.05020137665166, 28.72237493807718 41.04976969941787, 28.70440783159072 41.05233642891598, 28.68813243318253 41.05814657114341, 28.6731637334279 41.06689095186521, 28.63178688722385 41.10111595633148, 28.61670735142272 41.11008784262246, 28.59980193759226 41.11650466636763, 28.58401071770303 41.11890805853398, 28.56900118361548 41.11740302169191, 28.55487250442387 41.11210622536409, 28.54172384922239 41.10312267212088, 28.50934222321385 41.07086938258722, 28.49754110099887 41.06122664654109, 28.45895265638591 41.04810132524416, 28.41954752511447 41.05514233093545, 28.34467485896067 41.09128071557295, 28.32422269164197 41.09865422940379, 28.30342051575539 41.1028893330756, 28.23799808093537 41.10794112340589, 28.21626254886766 41.11177955070072, 28.19565287769341 41.11904806196116, 28.17655991031349 41.13106502279301, 28.13654809752432 41.17176518576573, 28.12198190762278 41.18402131911901, 28.09966886141801 41.19647579066077, 28.07550076980326 41.2045726555319, 28.05030598638928 41.2093327720556, 27.94564175762953 41.21749380516425, 27.91979362488878 41.22332144782006, 27.8962030474111 41.23205999506577, 27.71423942642663 41.33321830467018, 27.4106419946145 41.45701050166669, 27.38315465508066 41.46510153306173, 27.35529397307438 41.47038082896118, 27.25173810477969 41.48111442504397, 27.22152069841611 41.48690706684305, 27.21800311230854 41.48685456555782, 27.17473621983773 41.48228695374651, 27.16446346836932 41.48265446274283, 27.144512979998 41.48560036818947, 27.12185575870144 41.49102550099218, 27.08483068569182 41.50443082914345)'), {u'labelrank': 5, u'length_km': 385, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'E', u'continent': u'Asia', u'namealtt': u'', u'localalt': u'3', u'question': 0, u'sov_a3': u'', u'label': u'E80', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 1, u'local': u'3', u'edited': u'New in version 2.0.0', u'label2': u'3', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'80', u'level': u'E', u'type': u'Major Highway', u'routeraw': u'E80  0 3', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(11, wkt_loads('LINESTRING (-2.831886233941098 51.59774165498138, -2.762825168383762 51.62152182043337, -2.745041816395453 51.6245377275936, -2.727332841227827 51.62516774301581, -2.70967636734539 51.62352853622274, -2.692040310629418 51.61973677673696, -2.662218122273782 51.60693813010343, -2.635709348361084 51.58797641593647, -2.58760942091494 51.54348449347795)'), {u'labelrank': 6, u'length_km': 29, u'scalerank': 6, u'min_zoom': 6, u'prefix': u'', u'continent': u'Europe', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'E30', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 1, u'local': u'M48', u'edited': u'New in version 2.0.0', u'label2': u'M48', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'', u'level': u'', u'type': u'Major Highway', u'routeraw': u'E30 M4', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(12, wkt_loads('LINESTRING (-0.5261231241149692 51.4942207875435, -0.3150592074461678 51.49023068986919)'), {u'labelrank': 7, u'length_km': 23, u'scalerank': 6, u'min_zoom': 6, u'prefix': u'E', u'continent': u'Europe', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'E30', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 0, u'local': u'M4', u'edited': u'New in version 2.0.0', u'label2': u'M4', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'30', u'level': u'E', u'type': u'Secondary Highway', u'routeraw': u'E30 M4', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(13, wkt_loads('LINESTRING (-2.679400626220485 51.4974000320354, -2.675366777475227 51.47977126716462, -2.667997638751515 51.46380504299139, -2.654673979266113 51.45089556031137, -2.632770734759606 51.44243118644388)'), {u'labelrank': 7, u'length_km': 7, u'scalerank': 8, u'min_zoom': 7.1, u'prefix': u'E', u'continent': u'Europe', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'E30', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 0, u'local': u'M4', u'edited': u'New in version 2.0.0', u'label2': u'M4', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'30', u'level': u'E', u'type': u'Secondary Highway', u'routeraw': u'E30 M4', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(14, wkt_loads('LINESTRING (-80.9544063686898 33.97327267300678, -80.93796079435347 33.95832215088284, -80.90656469789322 33.94486668097131, -80.87666365364534 33.94337162875891, -80.86320818373379 33.94785678539608, -80.82732693063636 33.95234194203326, -80.78845557311411 33.93888647212172, -80.75855452886626 33.94636173318368, -80.7062277014325 33.93888647212172, -80.69725738815814 33.94187657654653, -80.65091076957394 33.94337162875891, -80.62848498638803 33.94636173318368)'), {u'labelrank': 0, u'length_km': 37, u'scalerank': 7, u'min_zoom': 7, u'prefix': u'US', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'USA', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'north_america_extra', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 3661, u'namealt': u'', u'uident': 33859, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'76', u'level': u'Federal', u'type': u'Secondary Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}), dsl.way(15, wkt_loads('LINESTRING (174.5957554559066 -36.7996459594322, 174.6195657602906 -36.84723778745579, 174.6690031436346 -36.8662554382397, 174.6753485926443 -36.87836013893899, 174.7108347756951 -36.88374749727563, 174.7549897714249 -36.86568011316013)'), {u'labelrank': 0, u'length_km': 18, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'', u'continent': u'Oceania', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'SH16', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'global_basic', u'toll': 0, u'expressway': 1, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 36958, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 71273, u'name': u'', u'level': u'Federal', u'type': u'Major Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}))

    def test_tch(self):
        # Trans-Canada Highway
        self.assert_has_feature(
            7, 20, 43, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'CA:??:primary',
             'kind': 'highway', 'shield_text': '1'})

    def test_i20(self):
        # I-20
        self.assert_has_feature(
            7, 35, 51, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'US:I',
             'kind': 'highway', 'shield_text': '20'})

    @unittest.skip(BROKEN)
    def test_us76(self):
        # US-76
        self.assert_has_feature(
            7, 35, 51, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'US:US',
             'kind': 'major_road', 'shield_text': '76'})

    def test_mex49(self):
        # MEX 49 (interstate)
        self.assert_has_feature(
            7, 27, 55, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'MX',
             'kind': 'highway', 'shield_text': '49'})

    @unittest.skip(BROKEN)
    def test_mex54(self):
        # MEX 54 (federal)
        self.assert_has_feature(
            7, 27, 55, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'MX:MX',
             'kind': 'major_road', 'shield_text': '54'})

    def test_e80(self):
        # E80 in Turkey
        self.assert_has_feature(
            7, 74, 47, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'e-road',
             'kind': 'highway', 'shield_text': '80'})

    def test_e30_m4(self):
        # E30 (M4) in UK
        self.assert_has_feature(
            7, 63, 42, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'e-road',
             'kind': 'highway', 'shield_text': '30'})

    def test_sh16(self):
        # SH16 in NZ
        self.assert_has_feature(
            7, 126, 78, 'roads',
            {'source': 'naturalearthdata.com', 'network': 'NZ:SH',
             'kind': 'highway', 'shield_text': '16'})
