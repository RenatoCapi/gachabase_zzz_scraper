import json
import os
from pathlib import Path
import re
import shutil
import time
import traceback

import requests
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from gachabase_webscraper import start_session
import logger_provider
from util import find_wengine_id, float_to_int, text_to_float
from wengines.wengine_constants import (
    BASEDATA_XPATH,
    EFFECT_XPATH,
    GACHABASE_URL_WENGINES,
    IMAGE_XPATH,
    METADATA_XPATH,
    NAME_XPATH,
    PARAM_LIST_WENGINE,
    POTENCIAL_BUTTON5_XPATH,
    STATS_BASE_XPATH,
)

from browser_manager import click_on_button, load_page, stop_session
from constants import (
    RARITY_ID,
    STATS_BASE_ID,
    STATS_FLOAT_ROUND,
    URL_BASE_GACHABASE,
    WEAPON_TYPE_ID,
)
from xpath_constants import XPATH_CLOSE_BUTTON_1, XPATH_CLOSE_BUTTON_2

logger = logger_provider.get_logger()

WENGINES_FOLDER = "/app/output/wengines/wengines_data"
WENGINES_ICON_FOLDER = "/app/output/wengines/wengines_icon"


def write_all_wengines():
    for url in GACHABASE_URL_WENGINES:
        _write_wengine_file(url)


def write_wengine(index):
    _write_wengine_file(GACHABASE_URL_WENGINES[index])


def _write_wengine_file(wengine_url):
    pattern_char_id = r"/w-engines/(\d{5})/"
    match_char_id = re.search(pattern_char_id, wengine_url)
    wengine_id = match_char_id.group(1)  # type: ignore

    try:
        wengine = _get_wengine(wengine_url)

        file_name = f"{wengine_id}.json"
        complete_path = os.path.join(WENGINES_FOLDER, file_name)

        logger.warning("escrevendo no caminho %s", complete_path)

        with open(complete_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(wengine))

    except Exception:
        logger.error("wengine - id: %s", wengine_id)
        traceback.print_exc()


def _get_wengine(wengine_url):
    browser: WebDriver = load_page(URL_BASE_GACHABASE + wengine_url)
    try_click_buttom(browser, XPATH_CLOSE_BUTTON_1)
    try_click_buttom(browser, XPATH_CLOSE_BUTTON_2)
    wengine = _get_wengine_metadata(browser)
    stop_session()

    return wengine


def try_click_buttom(browser, xpath):
    try:
        button = browser.find_element(By.XPATH, xpath)
        if button is not None:
            click_on_button(button)

    except Exception:
        logger.warning("erro ao clicar no botão: %s", xpath)


def _get_wengine_metadata(browser):
    core_element = browser.find_element(By.XPATH, BASEDATA_XPATH)
    wengine = {}
    wengine["name"] = core_element.find_element(By.XPATH, NAME_XPATH).text
    metadata_parent = core_element.find_element(By.XPATH, METADATA_XPATH)
    wengine["id"] = find_wengine_id(
        metadata_parent.find_element(By.XPATH, "./div").text
    )
    metadata_list_a = core_element.find_elements(By.TAG_NAME, "a")
    wengine["rarity"] = RARITY_ID[metadata_list_a[0].text]
    wengine["weaponType"] = WEAPON_TYPE_ID[metadata_list_a[1].text]
    wengine["stats"] = _get_wengine_stats(core_element)
    wengine["effect"] = _wengine_effect(core_element)
    wengine["imgUrl"] = _img_url(browser, wengine["id"])

    return wengine


def _get_wengine_stats(core_element):
    stat_list = core_element.find_elements(By.XPATH, STATS_BASE_XPATH)
    stats = {}
    for stat in stat_list:
        stat_element = stat.find_elements(By.TAG_NAME, "span")
        stat_id = STATS_BASE_ID.get(stat_element[0].text)
        stat_id = stat_id if stat_id is not None else "0"
        stats[stat_id] = _fix_stat_data(stat_id, stat_element[1].text)

    return stats


def _fix_stat_data(stat_id, raw_data):
    stat_value = text_to_float(raw_data)
    stat_value = (
        int(stat_value)
        if not stat_id in STATS_FLOAT_ROUND
        else float_to_int(stat_value)
    )

    return stat_value


def _wengine_effect(core_element):
    effect_elements = core_element.find_elements(By.XPATH, EFFECT_XPATH)
    effect = {}
    effect["name"] = effect_elements[0].text
    effect_desc = []
    effect_html = (
        effect_elements[1].find_element(By.XPATH, "./span").get_attribute("outerHTML")
    )
    effect_desc.append(str(BeautifulSoup(effect_html, "html.parser")))

    button = effect_elements[0].find_element(By.XPATH, POTENCIAL_BUTTON5_XPATH)
    click_on_button(button)
    effect_html = (
        effect_elements[1].find_element(By.XPATH, "./span").get_attribute("outerHTML")
    )
    effect_desc.append(str(BeautifulSoup(effect_html, "html.parser")))
    effect["desc"] = effect_desc
    return effect


def _img_url(browser: WebDriver, wengine_id: str):
    try:
        img_element = browser.find_element(By.XPATH, IMAGE_XPATH)
        src: str = img_element.get_attribute("src")  # type: ignore
        response = requests.get(src, stream=True, timeout=60)

        file_name = f"wengine_{wengine_id}.png"
        complete_path = os.path.join(WENGINES_ICON_FOLDER, file_name)

        logger.warning("escrevendo imagem no caminho %s", complete_path)

        with open(complete_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)

        return file_name
    except Exception:
        logger.error("erro ao salvar o png!")
        traceback.print_exc()
        return ""


def _get_wengines_url_list(browser):
    try:
        start_session()
        logger.warning("acessando a url: %s", URL_BASE_GACHABASE + PARAM_LIST_WENGINE)
        browser.get(URL_BASE_GACHABASE + PARAM_LIST_WENGINE)
        time.sleep(6)
        html_source = browser.page_source
        soup = BeautifulSoup(html_source, "html.parser")
        browser.quit()
        links_list_soup = soup.find("div", id="entries").find_all("a")  # type: ignore
        wengine_url_list = []

        for url_char in links_list_soup:
            wengine_url_list.append(url_char["href"])  # type: ignore

        return wengine_url_list
    except Exception as e:
        logger.error("url: %s - %s", URL_BASE_GACHABASE + PARAM_LIST_WENGINE, e)
        traceback.print_exc()
        return []
