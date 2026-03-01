CHAR_ID_LIST = [
    "1501",
    "1491",
    "1431",
    "1341",
    "1481",
    "1471",
    "1451",
    "1051",
    "1441",
    "1301",
    "1461",
    "1401",
    "1411",
    "1391",
    "1371",
    "1421",
    "1291",
    "1331",
    "1361",
    "1381",
    "1351",
    "1321",
    "1311",
    "1201",
    "1091",
    "1161",
    "1221",
    "1171",
    "1071",
    "1261",
    "1251",
    "1271",
    "1241",
    "1211",
    "1191",
    "1181",
    "1141",
    "1041",
    "1021",
    "1101",
    "1281",
    "1111",
    "1131",
    "1081",
    "1061",
    "1121",
    "1151",
    "1031",
    "1011",
]

GACHABASE_URL_CHARS = [
    "/agents/1501/aria3?lang=en&branch=release",
    "/agents/1491/sunna?lang=en&branch=release",
    "/agents/1431/ye-shunguang?lang=en&branch=release",
    "/agents/1341/zhao?lang=en&branch=release",
    "/agents/1481/dialyn?lang=en&branch=release",
    "/agents/1471/banyue?lang=en&branch=release",
    "/agents/1451/lucia-elowen?lang=en&branch=release",
    "/agents/1051/yidhari-murphy?lang=en&branch=release",
    "/agents/1441/komano-manato?lang=en&branch=release",
    "/agents/1301/orphie-magnusson-magus?lang=en&branch=release",
    "/agents/1461/seed?lang=en&branch=release",
    "/agents/1401/alice-thymefield?lang=en&branch=release",
    "/agents/1411/ukinami-yuzuha?lang=en&branch=release",
    "/agents/1391/ju-fufu?lang=en&branch=release",
    "/agents/1371/yixuan?lang=en&branch=release",
    "/agents/1421/pan-yinhu?lang=en&branch=release",
    "/agents/1291/hugo-vlad?lang=en&branch=release",
    "/agents/1331/vivian-banshee?lang=en&branch=release",
    "/agents/1361/trigger?lang=en&branch=release",
    "/agents/1381/soldier-0-anby?lang=en&branch=release",
    "/agents/1351/pulchra-fellini?lang=en&branch=release",
    "/agents/1321/evelyn-chevalier?lang=en&branch=release",
    "/agents/1311/astra-yao?lang=en&branch=release",
    "/agents/1201/asaba-harumasa?lang=en&branch=release",
    "/agents/1091/hoshimi-miyabi?lang=en&branch=release",
    "/agents/1161/lighter?lang=en&branch=release",
    "/agents/1221/tsukishiro-yanagi?lang=en&branch=release",
    "/agents/1171/burnice-white?lang=en&branch=release",
    "/agents/1071/caesar-king?lang=en&branch=release",
    "/agents/1261/jane-doe?lang=en&branch=release",
    "/agents/1251/qingyi?lang=en&branch=release",
    "/agents/1271/seth-lowell?lang=en&branch=release",
    "/agents/1241/zhu-yuan?lang=en&branch=release",
    "/agents/1211/alexandrina-sebastiane?lang=en&branch=release",
    "/agents/1191/ellen-joe?lang=en&branch=release",
    "/agents/1181/grace-howard?lang=en&branch=release",
    "/agents/1141/von-lycaon?lang=en&branch=release",
    "/agents/1041/soldier-11?lang=en&branch=release",
    "/agents/1021/nekomiya-mana?lang=en&branch=release",
    "/agents/1101/koleda-belobog?lang=en&branch=release",
    "/agents/1281/piper-wheel?lang=en&branch=release",
    "/agents/1111/anton-ivanov?lang=en&branch=release",
    "/agents/1131/soukaku?lang=en&branch=release",
    "/agents/1081/billy-kid?lang=en&branch=release",
    "/agents/1061/corin-wickes?lang=en&branch=release",
    "/agents/1121/ben-bigger?lang=en&branch=release",
    "/agents/1151/luciana-de-montefio?lang=en&branch=release",
    "/agents/1031/nicole-demara?lang=en&branch=release",
    "/agents/1011/anby-demara?lang=en&branch=release",
]

URL_BASE_GACHABASE = "https://zzz.gachabase.net"

PARAM_LIST_AGENTS = "agents?lang=en&branch=release"

HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        + "Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
    ),
    "Referer": "https://zzz.gachabase.net/",
}

RARITY_ID = {
    "S Rank": "4",
    "A Rank": "3",
}

WEAPON_TYPE_ID = {
    "Attack": "1",
    "Stun": "2",
    "Anomaly": "3",
    "Support": "4",
    "Defense": "5",
    "Rupture": "6",
}

HIT_TYPE_ID = {
    "Slash": "101",
    "Strike": "102",
    "Pierce": "103",
}

ELEMENT_TYPE_ID = {
    "Physical": "200",
    "Honed Edge": "200",
    "Fire": "201",
    "Ice": "202",
    "Frost": "202",
    "Electric": "203",
    "Ether": "205",
    "Auric Ink": "205",
}

CAMP_ID = {
    "none": "",
    "cunning": "1",
    "victoria": "2",
    "belobog": "3",
    "sons": "4",
    "defense": "5",
    "hollow": "6",
    "criminal": "7",
    "stars": "8",
    "mockingbird": "9",
    "yunkui": "10",
    "spook": "11",
    "krampus": "12",
    "angels": "13",
}

STATS_BASE_ID = {
    "Base HP": "11101",
    "Percent HP": "11102",
    "Base ATK": "12101",
    "Percent ATK": "12102",
    "Base DEF": "13101",
    "Percent DEF": "13102",
    "Base Impact": "12201",
    "Base Energy Regen": "30501",
    "CRIT Rate": "20101",
    "CRIT DMG": "21101",
    "PEN Ratio": "23101",
    "Anomaly Mastery": "31201",
    "Anomaly Proficiency": "31401",
    "Sheer Force": "12301",
    "Automatic Adrenaline Accumulation": "32001",
}

STATS_FLOAT_ROUND = [
    "30501",
    "20101",
    "21101",
    "23101",
    "32001",
    "11102",
    "12102",
    "13102",
]

BASE_ATTR_ID = ["11101", "12101", "13101"]
