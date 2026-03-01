import logging
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

from util import float_to_int, text_to_int
from xpath_constants import *


def get_char_skillkit(char, browser_instance):
    global browser
    global hit_map_aux

    browser = browser_instance
    skillkit = {}
    hit_map_aux = {}

    for skill_id in range(5):
        logging.info(
            "------------------- %s -------------------",
            GAMEGACHA_SKILLS_SECTION_MAP[skill_id],
        )
        skillkit[GAMEGACHA_SKILL_MAP[skill_id]] = _get_skill_data(skill_id)

    char["skillKit"] = skillkit
    char["hitMap"] = hit_map_aux
    return char


def _get_skill_data(skill_id: int):
    element_skills = browser.find_element(By.XPATH, get_skill_xpath(skill_id + 1))
    elements_desc = element_skills.find_element(By.XPATH, XPATH_SKILL_DESCS)

    desc = []

    logging.info("pegando descrição da skill...")
    for element_desc in elements_desc.find_elements(By.CLASS_NAME, "text-sm "):
        element_html = element_desc.get_attribute("outerHTML")
        desc.append(str(BeautifulSoup(element_html, "html.parser")))

    return {
        "skillId": GAMEGACHA_SKILL_MAP[skill_id],
        "desc": desc,
        "subSkills": _get_sub_skills_data(element_skills),
    }


def _get_sub_skills_data(element_skills):
    sub_skills_data = element_skills.find_elements(By.XPATH, XPATH_SUB_SKILLS_DATA)
    sub_skills = {}

    logging.info("iniciando manipulação do slider de lvl...")
    slider = sub_skills_data[0].find_element(By.XPATH, XPATH_SLIDER_KNOB)
    action = ActionChains(browser)

    _slider_move(action, slider, Keys.ARROW_LEFT)
    _get_sub_skills_per_lvl(sub_skills_data, sub_skills)

    _slider_move(action, slider, Keys.ARROW_RIGHT)
    _get_sub_skills_per_lvl(sub_skills_data, sub_skills)

    return sub_skills


def _get_sub_skills_per_lvl(sub_skills_data, sub_skills):
    for index, sub_skill_data in enumerate(sub_skills_data):
        if index & 1 == 0:
            sub_skill_id_raw = sub_skill_data.find_element(By.XPATH, "./h3").text
            sub_skill_id = re.sub(r":?\sSTATS$", "", sub_skill_id_raw)

            logging.info("pegando %s...", sub_skill_id)
        else:
            if sub_skill_id not in sub_skills:
                sub_skills[sub_skill_id] = {}

            _get_complex_hits_data(
                sub_skill_data, sub_skill_id, sub_skills[sub_skill_id]
            )


def _slider_move(action, slider, arrow):
    try:
        slider.click()
    except Exception as e:
        logging.warning(e)

    for _ in range(15):
        action.send_keys(arrow)

    action.perform()
    slider_index = slider.get_attribute("aria-valuenow")
    logging.info("Skill lvl - %s", slider_index)


def _get_complex_hits_data(sub_skill_data, sub_skill_id, sub_skill):
    logging.info("construindo subSkill %s...", sub_skill_id)
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
        formula_result = tds_soup[1].contents[2].span.get_text(strip=True)  # type: ignore

        if not raw_name[1]:
            continue

        hit_type = raw_name[1].lower()

        if not raw_name[0]:
            complex_hit_id = sub_skill_id + raw_name[2]
        else:
            complex_hit_id = raw_name[0] + raw_name[2]

        if complex_hit_id in sub_skill:
            sub_skill[complex_hit_id][hit_type].append(formula_result)

        else:
            sub_skill[complex_hit_id] = {"hitID": raw_ids, "dmg": [], "daze": []}
            sub_skill[complex_hit_id][hit_type].append(formula_result)

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

        dmg = float(tds_soup[0].get_text(strip=True).rstrip("%"))
        daze = float(tds_soup[1].get_text(strip=True).rstrip("%"))
        anomaly_buildup = text_to_int(tds_soup[3].get_text(strip=True))
        miasma_depletion = text_to_int(tds_soup[-1].get_text(strip=True))

        if simple_hit_id in hit_map_aux:
            if isinstance(hit_map_aux[simple_hit_id]["daze"], dict):
                continue

            hit_map_aux[simple_hit_id]["dmg"].append(dmg)
            hit_map_aux[simple_hit_id]["daze"].append(daze)
        else:
            hit_map_aux[simple_hit_id] = {
                "anomalyBuildup": anomaly_buildup,
                "miasmaDepletion": miasma_depletion,
                "dmg": [dmg],
                "daze": [daze],
            }

        if len(hit_map_aux[simple_hit_id]["daze"]) == 2:
            hit_map_aux[simple_hit_id]["dmg"] = get_multiplier(
                hit_map_aux[simple_hit_id]["dmg"][1],
                hit_map_aux[simple_hit_id]["dmg"][0],
            )
            hit_map_aux[simple_hit_id]["daze"] = get_multiplier(
                hit_map_aux[simple_hit_id]["daze"][1],
                hit_map_aux[simple_hit_id]["daze"][0],
            )


def get_multiplier(final: float, base: float):
    growth = float_to_int((final - base) / 15)
    return {"base": float_to_int(base), "growth": growth}
