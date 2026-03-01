import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from constants import BASE_ATTR_ID, STATS_BASE_ID, STATS_FLOAT_ROUND
from util import float_to_int, text_to_float
from xpath_constants import XPATH_BASE_CHAR_LVL_SLIDER


def get_statsbase(char, metadata_element, browser):
    stats_elements = metadata_element.find_elements(By.XPATH, "./div[3]/div/div")
    action = ActionChains(browser)
    slider_char_lvl = metadata_element.find_element(
        By.XPATH, XPATH_BASE_CHAR_LVL_SLIDER
    )

    char["growthStat"] = get_growth_stats(stats_elements, action, slider_char_lvl)
    char["staticStats"] = get_static_stats(stats_elements)
    return char


def get_static_stats(stats_elements):
    logging.info("pegando static stats...")
    static_stats = {}
    for index in range(3, len(stats_elements)):
        stat_element = stats_elements[index].find_elements(By.TAG_NAME, "span")
        stat_id = STATS_BASE_ID[stat_element[0].text]
        stat_value = text_to_float(stat_element[1].text)
        stat_value = (
            int(stat_value)
            if not stat_id in STATS_FLOAT_ROUND
            else float_to_int(stat_value)
        )

        static_stats[stat_id] = stat_value

    return static_stats


def get_growth_stats(element_stats, action, slider_char_lvl):
    logging.info("pegando stats que tem scaling por lvl...")
    lvl60 = get_raw_lvl_stat(element_stats)
    back_slider(action, slider_char_lvl, 54)
    lvl11 = get_raw_lvl_stat(element_stats)
    back_slider(action, slider_char_lvl, 1)
    lvl10 = get_raw_lvl_stat(element_stats)
    back_slider(action, slider_char_lvl, 9)
    lvl1 = get_raw_lvl_stat(element_stats)

    growth_stats = {}
    for index, value in enumerate(BASE_ATTR_ID):
        # corrigir atk base sem core lvl
        if value == "12101":
            lvl60[index] -= 75

        growth_stats[value] = get_growth_stat(
            lvl60[index], lvl11[index], lvl10[index], lvl1[index]
        )

    return growth_stats


def get_raw_lvl_stat(stats_growth_element) -> list[int]:
    lvl_stat: list[int] = []
    for index in range(3):
        span_element = stats_growth_element[index].find_elements(By.TAG_NAME, "span")
        lvl_stat.append(int(span_element[1].text))

    return lvl_stat


def get_growth_stat(lvl60, lvl11, lvl10, lvl1):
    stat_base = lvl1
    asc_growth = lvl11 - lvl10
    stat_growth = float_to_int((lvl60 - asc_growth * 5 - stat_base) / (60 - 1))

    return {"base": stat_base, "growth": stat_growth, "asc": asc_growth}


def back_slider(action, slider, back_lvl):
    try:
        slider.click()
    except Exception as e:
        logging.warning(e)

    for _ in range(back_lvl):
        action.send_keys(Keys.ARROW_LEFT)

    action.perform()
    logging.info("Slider lvl - %s", slider.get_attribute("aria-valuenow"))
