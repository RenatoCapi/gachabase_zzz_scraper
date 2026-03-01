import json
import logging
import os
import re
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests

from parsers.skillkit_parser import get_char_skillkit
from parsers.metadata_parser import get_metadata
from constants import *
from util import float_to_int, text_to_float
from xpath_constants import *

logging.basicConfig(
    stream=sys.stdout,
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def start_session():
    global browser

    logging.info("abrindo o browser...")
    options = webdriver.ChromeOptions()  # type: ignore
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Remote("http://172.17.0.2:4444/wd/hub", options=options)  # type: ignore


def _get_char(char_url):
    load_character_page(char_url)
    close_dialog()

    char = get_metadata(browser)
    char = get_char_skillkit(char, browser)
    char = _get_core(char)

    browser.quit()

    return char


def _get_core(char):
    core_element = browser.find_element(By.XPATH, XPATH_CORE)
    core_elements_desc = core_element.find_elements(By.XPATH, "./div[1]")
    desc = []

    for element_desc in core_elements_desc:
        element_html = element_desc.get_attribute("outerHTML")
        desc.append(str(BeautifulSoup(element_html, "html.parser")))

    core_elements_stats = core_element.find_elements(By.XPATH, "./div[2]/div")
    core_growth_stats = {}
    for stats in core_elements_stats:
        texts_core = stats.find_elements(By.TAG_NAME, "span")
        core_growth_stats[STATS_BASE_ID[texts_core[0].text]] = text_to_float(
            texts_core[1].text
        )

    for index, _ in core_growth_stats.items():
        core_growth_stats[index] /= 3
        if index in STATS_FLOAT_ROUND:
            core_growth_stats[index] = float_to_int(core_growth_stats[index])
        else:
            core_growth_stats[index] = int(core_growth_stats[index])

    char["coreSkill"] = {"desc": desc, "coreGrowthStat": core_growth_stats}
    return char


def load_character_page(char_url):
    try:
        start_session()
        logging.warning("acessando a url: %s", URL_BASE_GACHABASE + char_url)
        browser.get(URL_BASE_GACHABASE + char_url)
    except Exception as e:
        logging.error("personagem - url: %s", URL_BASE_GACHABASE + char_url)
        traceback.print_exc()


def close_dialog():
    try:
        close_button = browser.find_element(By.XPATH, XPATH_CLOSE_BUTTON)
        action = ActionChains(browser)
        action.click(close_button).perform()
    except Exception:
        traceback.print_exc()


def write_char(index):
    try:
        char = _get_char(GACHABASE_URL_CHARS[index])
        folder_path = "/app/output"
        file_name = f"{CHAR_ID_LIST[index]}.json"
        complete_path = os.path.join(folder_path, file_name)

        logging.warning("escrevendo no caminho %s", complete_path)

        with open(complete_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(char))

    except Exception:
        logging.error("personagem - id: %s", CHAR_ID_LIST[index])
        traceback.print_exc()


def write_all_chars():
    for index in range(21, len(GACHABASE_URL_CHARS)):
        write_char(index)


# usado uma vez pra pegar o mapa de urls
def _get_char_url_list():
    content = _request_html_content(URL_BASE_GACHABASE + PARAM_LIST_AGENTS)
    soup = BeautifulSoup(content)
    links_list_soup = soup.find("div", id="entries").find_all("a")  # type: ignore
    char_url_list = []
    for url_char in links_list_soup:
        char_url_list.append(url_char["href"])  # type: ignore

    return char_url_list


def _request_html_content(url: str):
    resp = requests.get(url, headers=HEADERS, timeout=5)
    return resp.content


if __name__ == "__main__":
    write_char(0)
