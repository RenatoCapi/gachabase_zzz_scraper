GAMEGACHA_SKILL_MAP = {
    1: 0,
    2: 2,
    3: 6,
    4: 1,
    5: 3,
    6: 5
}
#BASE                                                                    SUBSKILLS 
"/html/body/div[1]/div[1]/main/article/section[2]"
#skill_raw
"/div/section[{X}]"
#skill_data
"/div[2]/div[2]/div"


XPATH_GAMEGACHA_SKILLS = "/html/body/div[1]/div[1]/main/article/section[2]"

GAMEGACHA_SKILLS_SECTION_MAP = {
    "BASIC":"1",
    "DODGE":"2",
    "ASSIST":"3",
    "SPECIAL":"4",
    "CHAIN":"5",
}

XPATH_SKILL_TITLE_ID = 1
SKILL_DATA_ID = 2

def _get_skill_xpath(id:int) -> str:
    return f"/div/section[{id}]"

XPATH_SKILL_DESCS = "/div[2]/div[1]"
def _get_skill_desc_xpath(id:int):
    return f"/div[{id}]"

XPATH_SKILL_DATA = "/div[2]/div[2]/div"

SUBSKILL_DESC = 1
SUBSKILL_DATA = 2
def _get_subskill_xpath(id:int) -> str:
    return f"/div[{id}]"


HIT_TITLE_ID = 1
HIT_DATA_ID = 2
def _get_hit_xpath(id:int):
    return f"/div[2]/div/div[{id}]"

HIT_NAMES = "/div[1]"
HIT_DATA = "/div[2]"
