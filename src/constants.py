GACHABASE_URL_CHARS = [
    "/agents/1621/roxy/release?lang=en",
    "/agents/1611/claret/release?lang=en",
    "/agents/1591/sigrid/release?lang=en",
    "/agents/1581/remielle/release?lang=en",
    "/agents/1571/norma/release?lang=en",
    "/agents/1561/velina/release?lang=en",
    "/agents/1551/pyrois/release?lang=en",
    "/agents/1541/promeia/release?lang=en",
    "/agents/1531/starlight-billy/release?lang=en",
    "/agents/1521/cissia/release?lang=en",
    "/agents/1511/nangong-yu/release?lang=en",
    "/agents/1501/aria/release?lang=en",
    "/agents/1491/sunna/release?lang=en",
    "/agents/1481/dialyn/release?lang=en",
    "/agents/1471/banyue/release?lang=en",
    "/agents/1461/seed/release?lang=en",
    "/agents/1451/lucia/release?lang=en",
    "/agents/1431/ye-shunguang/release?lang=en",
    "/agents/1411/yuzuha/release?lang=en",
    "/agents/1401/alice/release?lang=en",
    "/agents/1391/ju-fufu/release?lang=en",
    "/agents/1381/soldier-0-anby/release?lang=en",
    "/agents/1371/yixuan/release?lang=en",
    "/agents/1361/trigger/release?lang=en",
    "/agents/1341/zhao/release?lang=en",
    "/agents/1331/vivian/release?lang=en",
    "/agents/1321/evelyn/release?lang=en",
    "/agents/1311/astra-yao/release?lang=en",
    "/agents/1301/orphie-magus/release?lang=en",
    "/agents/1291/hugo/release?lang=en",
    "/agents/1261/jane/release?lang=en",
    "/agents/1251/qingyi/release?lang=en",
    "/agents/1241/zhu-yuan/release?lang=en",
    "/agents/1221/yanagi/release?lang=en",
    "/agents/1211/rina/release?lang=en",
    "/agents/1201/harumasa/release?lang=en",
    "/agents/1191/ellen/release?lang=en",
    "/agents/1181/grace/release?lang=en",
    "/agents/1171/burnice/release?lang=en",
    "/agents/1161/lighter/release?lang=en",
    "/agents/1141/lycaon/release?lang=en",
    "/agents/1101/koleda/release?lang=en",
    "/agents/1091/miyabi/release?lang=en",
    "/agents/1071/caesar/release?lang=en",
    "/agents/1051/yidhari/release?lang=en",
    "/agents/1041/soldier-11/release?lang=en",
    "/agents/1021/nekomata/release?lang=en",
    "/agents/1441/manato/release?lang=en",
    "/agents/1421/pan-yinhu/release?lang=en",
    "/agents/1351/pulchra/release?lang=en",
    "/agents/1281/piper/release?lang=en",
    "/agents/1271/seth/release?lang=en",
    "/agents/1151/lucy/release?lang=en",
    "/agents/1131/soukaku/release?lang=en",
    "/agents/1121/ben/release?lang=en",
    "/agents/1111/anton/release?lang=en",
    "/agents/1081/billy/release?lang=en",
    "/agents/1061/corin/release?lang=en",
    "/agents/1031/nicole/release?lang=en",
    "/agents/1011/anby/release?lang=en",
]

URL_BASE_GACHABASE = "https://zzz.gachabase.net"
PARAM_LIST_AGENTS = "/agents/release?lang=en"

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
    "B Rank": "2",
}

WEAPON_TYPE_ID = {
    "Attack": "1",
    "Stun": "2",
    "Anomaly": "3",
    "Support": "4",
    "Defense": "5",
    "Rupture": "6",
    "Armorer": "7",
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
    "Wind": "204",
    "Ether": "205",
    "Auric Ink": "205",
    "Lumiflux": "300",
}

CAMP_ID = {
    "none": "",
    "cunning": "1",
    "victoria": "2",
    "belobog": "3",
    "sons": "4",
    "defense": "5",
    "hollow": "6",
    "public": "7",
    "stars": "8",
    "mockingbird": "9",
    "yunkui": "10",
    "spook": "11",
    "krampus": "12",
    "angels": "13",
    "phaethon": "14",
    "roscaelifer": "15",
    "covenant": "16",
    "airspace": "17",
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
    "Energy Regen": "30502",
    "CRIT Rate": "20101",
    "CRIT DMG": "21101",
    "PEN Ratio": "23101",
    "Anomaly Mastery": "31401",
    "Anomaly Proficiency": "31201",
    "Sheer Force": "12301",
    "Automatic Adrenaline Accumulation": "32001",
    "Laceration DMG": "21301",
    "Automatic Sharpness Accumulation": "32401",
}

STATS_FLOAT_ROUND = [
    "30501",
    "30502",
    "20101",
    "21101",
    "23101",
    "32001",
    "11102",
    "12102",
    "13102",
    "21301",
]

BASE_ATTR_ID = ["11101", "12101", "13101"]
