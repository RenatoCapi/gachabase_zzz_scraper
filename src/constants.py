
CHAR_ID_LIST:list[str] = [
    "1061","1251","1261","1131","1081","1181","1011","1071","1031","1281","1021","1241","1141",
    "1111","1041","1121","1211","1151","1101","1221","1271","1171","1191","1161","1091","1201",
    "1311","1321","1381","1351","1361","1051","1291","1301","1341","1371","1391","1401","1411",
    "1421","1431","1441","1451","1461","1471","1481","1491","1501","1331"
]

CHAR_ID_LIST2 = [
    "1501","1491","1431","1341","1481","1471","1502","1451","1051","1441","1301","1461","1401",
    "1411","1391","1371","1421","1291","1331","1361","1381","1351","1321","1311","1201","1091",
    "1161","1221","1171","1071","1261","1251","1271","1241","1211","1191","1181","1141","1041",
    "1021","1101","1281","1111","1131","1081","1061","1121","1151","1031","1011"]

HOYO_SkillID = {
    0: "Basic",
    1: "Special",
    2: "Dodge",
    3: "Chain",
    5: "Core",
    6: "Assist",
}

GACHABASE_URL_CHARS = [ 
    '/agents/1501/aria3?lang=en&branch=beta', 
    '/agents/1491/sunna?lang=en&branch=beta', 
    '/agents/1431/ye-shunguang?lang=en&branch=beta', 
    '/agents/1341/zhao?lang=en&branch=beta', 
    '/agents/1481/dialyn?lang=en&branch=beta', 
    '/agents/1471/banyue?lang=en&branch=beta',
	'/agents/1502/aria6?lang=en&branch=beta',
	'/agents/1451/lucia-elowen?lang=en&branch=beta',
	'/agents/1051/yidhari-murphy?lang=en&branch=beta',
	'/agents/1441/komano-manato?lang=en&branch=beta',
	'/agents/1301/orphie-magnusson-magus?lang=en&branch=beta',
	'/agents/1461/seed?lang=en&branch=beta',
	'/agents/1401/alice-thymefield?lang=en&branch=beta',
	'/agents/1411/ukinami-yuzuha?lang=en&branch=beta',
	'/agents/1391/ju-fufu?lang=en&branch=beta',
	'/agents/1371/yixuan?lang=en&branch=beta',
	'/agents/1421/pan-yinhu?lang=en&branch=beta',
	'/agents/1291/hugo-vlad?lang=en&branch=beta',
	'/agents/1331/vivian-banshee?lang=en&branch=beta',
	'/agents/1361/trigger?lang=en&branch=beta',
	'/agents/1381/soldier-0-anby?lang=en&branch=beta',
	'/agents/1351/pulchra-fellini?lang=en&branch=beta',
	'/agents/1321/evelyn-chevalier?lang=en&branch=beta',
	'/agents/1311/astra-yao?lang=en&branch=beta',
	'/agents/1201/asaba-harumasa?lang=en&branch=beta',
	'/agents/1091/hoshimi-miyabi?lang=en&branch=beta',
	'/agents/1161/lighter?lang=en&branch=beta',
	'/agents/1221/tsukishiro-yanagi?lang=en&branch=beta',
	'/agents/1171/burnice-white?lang=en&branch=beta',
	'/agents/1071/caesar-king?lang=en&branch=beta',
	'/agents/1261/jane-doe?lang=en&branch=beta',
	'/agents/1251/qingyi?lang=en&branch=beta',
	'/agents/1271/seth-lowell?lang=en&branch=beta',
	'/agents/1241/zhu-yuan?lang=en&branch=beta',
	'/agents/1211/alexandrina-sebastiane?lang=en&branch=beta',
	'/agents/1191/ellen-joe?lang=en&branch=beta',
	'/agents/1181/grace-howard?lang=en&branch=beta',
	'/agents/1141/von-lycaon?lang=en&branch=beta',
	'/agents/1041/soldier-11?lang=en&branch=beta',
	'/agents/1021/nekomiya-mana?lang=en&branch=beta',
	'/agents/1101/koleda-belobog?lang=en&branch=beta',
	'/agents/1281/piper-wheel?lang=en&branch=beta',
	'/agents/1111/anton-ivanov?lang=en&branch=beta',
	'/agents/1131/soukaku?lang=en&branch=beta',
	'/agents/1081/billy-kid?lang=en&branch=beta',
	'/agents/1061/corin-wickes?lang=en&branch=beta',
	'/agents/1121/ben-bigger?lang=en&branch=beta',
	'/agents/1151/luciana-de-montefio?lang=en&branch=beta',
	'/agents/1031/nicole-demara?lang=en&branch=beta',
	'/agents/1011/anby-demara?lang=en&branch=beta']

URL_BASE_GACHABASE = "https://zzz.gachabase.net"

PARAM_LIST_AGENTS = "agents?lang=en&branch=beta"

HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " + 
        "Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
    ), 
    "Referer": "https://zzz.gachabase.net/"
}