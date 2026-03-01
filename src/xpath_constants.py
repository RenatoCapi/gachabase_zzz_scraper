GAMEGACHA_SKILL_MAP = [0, 2, 6, 1, 3, 5]


GAMEGACHA_SKILLS_SECTION_MAP = ["BASIC", "DODGE", "ASSIST", "SPECIAL", "CHAIN"]

XPATH_CLOSE_BUTTON = "/html/body/div[9]/div/div/button"

XPATH_BASE_GACHABASE_SKILLS = "/html/body/div[1]/div[1]/main/article/section[2]"


# XPATH_BASE_GAMEGACHA_SKILLS /
def get_skill_xpath(id: int) -> str:
    return f"{XPATH_BASE_GACHABASE_SKILLS}/div/section[{id}]"


# get_skill_xpath() /
XPATH_SKILL_DESCS = "./div[2]/div[1]"

# get_skill_xpath() /
XPATH_SUB_SKILLS_DATA = "./div[2]/div[2]/div/div"

# XPATH_SUB_SKILLS_DATA /
XPATH_SLIDER_KNOB = "./div/div[2]/div/div[2]"


XPATH_GACHABASE_META_DATA = (
    "/html/body/div[1]/div[1]/main/article/section[1]/div[2]/div"
)

# XPATH_BASE_GACHABASE_META_DATA /
XPATH_BASE_CHAR_LVL_SLIDER = "./div[1]/div[2]/div/div[2]"
XPATH_BASESTATS = "./div[3]/div"

XPATH_CORE = "/html/body/div[1]/div[1]/main/article/section[3]/div/section/div[2]"