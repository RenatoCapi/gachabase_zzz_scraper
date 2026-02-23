import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests

from constants import *
from xpath_constants import *
from xpath_constants import _get_skill_xpath

options = webdriver.ChromeOptions() # type: ignore
options.add_argument("--headless")
browser = webdriver.Remote("http://172.17.0.2:4444/wd/hub", options=options) # type: ignore

browser.maximize_window()

#usado uma vez pra pegar o mapa de urls
def _get_char_url_list():
    content = _request_html_content(URL_BASE_GACHABASE + PARAM_LIST_AGENTS)
    soup = BeautifulSoup(content)
    links_list_soup = soup.find('div', id="entries").find_all('a')  # type: ignore
    char_url_list = []
    for url_char in links_list_soup:
        char_url_list.append(url_char['href']) # type: ignore

    pass

def _request_html_content(url: str):
    resp = requests.get(url, headers=HEADERS, timeout=5)
    return resp.content

def _get_char_url(char_url:str) -> str:
    return f"{URL_BASE_GACHABASE}/{char_url}"

"""
def load_data():
    chars_skills_database: dict = {}
    for param_char_url in GACHABASE_URL_CHARS:
        chars_skills_database[param_char_url] = _get_char(param_char_url) # type: ignore
"""


def _get_char_skillkit(param_char_url):
    skillkit = {}
    browser.get(URL_BASE_GACHABASE + param_char_url)

    #fechar o dialog
    close_button = browser.find_element(By.ID, 'dialog:s34:close')
    action = ActionChains(browser)
    action.click(close_button).perform()

    for skill_id in range(1,5):
        skillkit[GAMEGACHA_SKILL_MAP[skill_id]] = _get_skill_data(skill_id)

    
    browser.quit()
    return skillkit
    selenium_basic = browser.find_element(By.XPATH, XPATH_GAMEGACHA_SKILLS)

    html_basic = selenium_basic.get_attribute('outerHTML')
    basic_soup = BeautifulSoup(html_basic, 'html.parser') 
    #action.click_and_hold(slider).move_by_offset(-25*11,0).release().perform()
    time.sleep(5)
    browser.quit()
    pass

def _get_skill_data(skill_id:int):
    elements_desc = browser.find_element(
        By.XPATH, XPATH_GAMEGACHA_SKILLS
        + _get_skill_xpath(skill_id)
        + XPATH_SKILL_DESCS
    )

    desc = []
    for element_desc in elements_desc.find_elements(By.CLASS_NAME,"text-sm "):
        element_html = element_desc.get_attribute("outerHTML")
        desc.append(str(BeautifulSoup(element_html,'html.parser')))

    return {
        "skillId":skill_id,
        "desc":desc,
        "subSkills": _get_sub_skills_data(skill_id)
    }

def _get_sub_skills_data(skill_id:int):
    xpath_sub_skill_data = XPATH_GAMEGACHA_SKILLS + _get_skill_xpath(skill_id) + XPATH_SKILL_DATA
    sub_skills_data = browser.find_elements(By.TAG_NAME,'div')
    sub_skills = {}
    sub_skill_id = ""

    for id, sub_skill_data in enumerate(sub_skills_data):
        if id & 1 == 0:
            sub_skill_id = sub_skills_data.find_element(By.TAG_NAME,"h3").text
        else:
            find_tables = sub_skill_data.find_elements(By.TAG_NAME,'tbody')
            

    return {}

def _get_complex_hit_data():

    pass

def _get_simple_hit_data(element_complex_hit_table):
    simpleHit = {
        "id": "",
        "energyGain": 0,
        "anomalyBuildup": 0,
        "decibelsGain": 0,
        "adrenalineGain": 0,
        "miasmaDepletion": 0,
        "dmg": [],
        "daze": [],
    }
    

    pass

if __name__ == "__main__":
    _get_char_skillkit(GACHABASE_URL_CHARS[0])
