import logging
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

from xpath_constants import *


def get_char_skillkit(char, browser_instance):
    global browser
    global hit_map_aux

    browser = browser_instance
    skillkit = {}
    hit_map_aux = {}

    for skill_id in range(5):
        logging.info(GAMEGACHA_SKILLS_SECTION_MAP[skill_id])
        skillkit[GAMEGACHA_SKILL_MAP[skill_id]] = _get_skill_data(skill_id)

    char["skillKit"] = skillkit
    char["hitMap"] = hit_map_aux
    return char


def _get_skill_data(skill_id: int):
    element_skills = browser.find_element(By.XPATH, get_skill_xpath(skill_id + 1))
    elements_desc = element_skills.find_element(By.XPATH, XPATH_SKILL_DESCS)

    desc = []

    logging.info(f"pegando descrição da skill...")
    for element_desc in elements_desc.find_elements(By.CLASS_NAME, "text-sm "):
        element_html = element_desc.get_attribute("outerHTML")
        desc.append(str(BeautifulSoup(element_html, "html.parser")))

    return {
        "skillId": GAMEGACHA_SKILL_MAP[skill_id],
        "desc": desc,
        "subSkills": _get_sub_skills_data(skill_id, element_skills),
    }


def _get_sub_skills_data(skill_id: int, element_skills):
    sub_skills_data = element_skills.find_elements(By.XPATH, XPATH_SUB_SKILLS_DATA)
    sub_skills = {}

    logging.info(f"iniciando manipulação do slider de lvl...")
    slider_knob = sub_skills_data[0].find_element(By.XPATH, XPATH_SLIDER_KNOB)
    action = ActionChains(browser)
    reset_slider(action, slider_knob)

    for _ in range(1, 17):
        _get_sub_skills_per_lvl(sub_skills_data, sub_skills)
        next_lvl(action, slider_knob)

    return sub_skills


def _get_sub_skills_per_lvl(sub_skills_data, sub_skills):
    for index, sub_skill_data in enumerate(sub_skills_data):
        if index & 1 == 0:
            sub_skill_id_raw = sub_skill_data.find_element(By.XPATH, "./h3").text
            sub_skill_id = re.sub(r":?\sSTATS$", "", sub_skill_id_raw)

            logging.info(f"pegando {sub_skill_id}...")
        else:
            if sub_skill_id not in sub_skills:
                sub_skills[sub_skill_id] = {}

            _get_complex_hits_data(
                sub_skill_data, sub_skill_id, sub_skills[sub_skill_id]
            )


def reset_slider(action, knob):
    try:
        knob.click()
    except Exception as e:
        logging.warning(e)

    for _ in range(16):
        action.send_keys(Keys.ARROW_LEFT)

    action.perform()
    logging.info(f"Slider resetado posição - {knob.get_attribute("aria-valuenow")}")


def next_lvl(action, knob):
    try:
        knob.click()
    except Exception as e:
        logging.warn(e)

    action.send_keys(Keys.ARROW_RIGHT).perform()
    slider_index = knob.get_attribute("aria-valuenow")
    logging.info(f"skill lvl - {slider_index}")


def _get_complex_hits_data(sub_skill_data, sub_skill_id, sub_skill):
    logging.info(f"construindo subSkill {sub_skill_id}...")
    tbodys_element = sub_skill_data.find_elements(By.TAG_NAME, "tbody")
    tr_elements = tbodys_element[0].find_elements(By.TAG_NAME, "tr")

    for tr in tr_elements:
        complex_hit_id = ""
        html_tr = tr.get_attribute("outerHTML")
        tds_soup = BeautifulSoup(html_tr, "html.parser").find_all("td")
        spans_name_soup = tds_soup[0].find_all("span")

        if len(spans_name_soup) < 2:
            continue

        raw_name = find_hit_complex_id(spans_name_soup[0].get_text(strip=True))  # type: ignore
        raw_ids = spans_name_soup[1].get_text(strip=True).split(", ")
        multiplier = tds_soup[1].contents[2].span.get_text(strip=True)  # type: ignore

        if not raw_name[1]:
            continue

        if not raw_name[0]:
            complex_hit_id = sub_skill_id
        else:
            complex_hit_id = raw_name[0] + raw_name[2]

        if complex_hit_id in sub_skill:
            sub_skill[complex_hit_id][raw_name[1].lower()].append(multiplier)

        else:
            sub_skill[complex_hit_id] = {"hitID": raw_ids, "dmg": [], "daze": []}
            sub_skill[complex_hit_id][raw_name[1].lower()].append(multiplier)

    if len(tbodys_element) == 2:
        _update_hit_map(tbodys_element[1])


def find_hit_complex_id(raw: str) -> tuple:
    pattern = r"^(.*?)\s*(DMG|Daze)\sMultiplier(.*)$"
    match = re.search(pattern, raw)
    if match:
        return match.groups()

    return ("", "", "")


def _update_hit_map(tbody_element):
    tr_elements = tbody_element.find_elements(By.TAG_NAME, "tr")
    for tr in tr_elements:
        html_tr = tr.get_attribute("outerHTML")
        th_soup = BeautifulSoup(html_tr, "html.parser").find("th")
        tds_soup = BeautifulSoup(html_tr, "html.parser").find_all("td")
        simple_hit_id = th_soup.get_text(strip=True)  # type: ignore

        if simple_hit_id in hit_map_aux:
            hit_map_aux[simple_hit_id]["dmg"].append(tds_soup[0].get_text(strip=True))
            hit_map_aux[simple_hit_id]["daze"].append(tds_soup[1].get_text(strip=True))
        else:
            hit_map_aux[simple_hit_id] = {
                "anomalyBuildup": tds_soup[3].get_text(strip=True),
                "miasmaDepletion": tds_soup[5].get_text(strip=True),
                "dmg": [tds_soup[0].get_text(strip=True)],
                "daze": [tds_soup[1].get_text(strip=True)],
            }
