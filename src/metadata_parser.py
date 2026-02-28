import logging
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from char_statsbase_parser import get_statsbase
from constants import *
from xpath_constants import XPATH_GACHABASE_META_DATA


def get_metadata(browser: WebElement):
    char = {}

    element_parent = browser.find_element(By.XPATH, XPATH_GACHABASE_META_DATA)
    elements_charbase_data = element_parent.find_elements(By.XPATH, "./div")
    char["name"] = elements_charbase_data[0].find_element(By.TAG_NAME, "h1").text

    logging.info(f"pegando metadata de {char["name"]}...")
    camp_raw = elements_charbase_data[0].find_element(By.TAG_NAME, "h2").text
    char["camp"] = CAMP_ID[_get_first_word(camp_raw)]

    char_metadata = elements_charbase_data[1].find_elements(By.TAG_NAME, "a")
    char["rarity"] = RARITY_ID[char_metadata[0].text]
    char["weaponType"] = WEAPON_TYPE_ID[char_metadata[2].text]
    char["ElementType"] = ELEMENT_TYPE_ID[char_metadata[3].text]
    char["hitType"] = [HIT_TYPE_ID[char_metadata[4].text]]
    if len(char_metadata) > 5:
        char["hitType"].append(HIT_TYPE_ID[char_metadata[5].text])

    char["id"] = _find_id(
        elements_charbase_data[1].find_element(By.XPATH, "./div").text
    )
    char = get_statsbase(char, elements_charbase_data[2], browser)
    return char


def _get_first_word(text: str):
    pattern = r"^(\S*)"
    match = re.search(pattern, text.lower())
    if match:
        return match.group(1)

    return "none"


def _find_id(text):
    pattern = r"(\d{4})"
    match = re.search(pattern, text)
    if match:
        return match.group(1)

    return ""
