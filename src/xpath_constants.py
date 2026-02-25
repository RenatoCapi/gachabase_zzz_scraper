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




XPATH_BASE_GAMEGACHA_SKILLS = "/html/body/div[1]/div[1]/main/article/section[2]"

XPATH_CLOSE_BUTTON = "/html/body/div[9]/div/div/button"

GAMEGACHA_SKILLS_SECTION_MAP = {
    1: "BASIC",
    2: "DODGE",
    3: "ASSIST",
    4: "SPECIAL",
    5: "CHAIN",
}

XPATH_SKILL_TITLE_ID = 1
SKILL_DATA_ID = 2

# XPATH_BASE_GAMEGACHA_SKILLS / 
def get_skill_xpath(id:int) -> str:
    return f"/div/section[{id}]"

# get_skill_xpath() /
XPATH_SKILL_DESCS = "./div[2]/div[1]"
def get_skill_desc_xpath(id:int):
    return f"/div[{id}]"

# get_skill_xpath() /
XPATH_SUB_SKILLS_DATA = "./div[2]/div[2]/div/div"

# XPATH_SUB_SKILLS_DATA /
XPATH_SLIDER_SUB_SKILLS = "./div/div[2]/div/div[2]"


def get_subskill_xpath(id:int) -> str:
    return f"/div[{id}]"

def get_hit_xpath(id:int):
    return f"/div[2]/div/div[{id}]"


