import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup, Tag
import requests

from constants import *


GAMEGACHA_SKILL_MAP = {
    0:"Basic Attack",
    2:"Dodge",
    6:"Assist",
    1:"Special Attack",
    3:"Chain Attack",
    5:"Core Skill"
}


XPATH_GAMEGACHA_SKILLS = "/html/body/div[1]/div[1]/main/article/section[2]"

GAMEGACHA_SKILLS_SECTION_MAP = {
    "BASIC":"1",
    "DODGE":"2",
    "ASSIST":"3",
    "SPECIAL":"4",
    "CHAIN":"5",
}

SKILL_TITLE_ID = 1
SKILL_DATA_ID = 2

def _get_skill_xpath(id:int) -> str:
    return f"/div/section[{id}]"

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


#usado 1x pra pegar o mapa de urls
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

def selenium_test():
    browser = webdriver.Chrome() # type: ignore
    browser.maximize_window()
    browser.get(URL_BASE_GACHABASE + GACHABASE_URL_CHARS[0])

    close_button = browser.find_element(By.ID, 'dialog:s34:close')
    action = ActionChains(browser)
    action.click(close_button).perform()
    slider = browser.find_element(By.ID, 'slider:s4:thumb:0')   
    action.click_and_hold(slider).move_by_offset(-25*11,0).release().perform()
    time.sleep(5)


    pass

"""
def load_data():
    chars_skills_database: dict = {}
    for param_char_url in GACHABASE_URL_CHARS:
        chars_skills_database[param_char_url] = _get_char(param_char_url) # type: ignore
"""
        
def _get_char(param_char_url):
    browser = webdriver.Chrome() # type: ignore
    browser.maximize_window()
    browser.get(URL_BASE_GACHABASE + param_char_url)

    #fechar o dialog
    close_button = browser.find_element(By.ID, 'dialog:s34:close')
    action = ActionChains(browser)
    action.click(close_button).perform()
    
    selenium_basic = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/article/section[2]/div/section[1]")
    "/html/body/div[1]/div[1]/main/article/section[2]/div/section[1]/div[2]/div[2]/div/div[2]"

    html_basic = selenium_basic.get_attribute('outerHTML')
    basic_soup = BeautifulSoup(html_basic, 'html.parser') 
    #action.click_and_hold(slider).move_by_offset(-25*11,0).release().perform()
    time.sleep(5)
    browser.quit()
    pass

def _get_skill_data(skill_id, skill_name, skill_table: Tag | None): 
    pass

def _get_sub_skills():
    pass

def _get_sub_skill_data(element_hits):


    pass

if __name__ == "__main__":
    _get_char(GACHABASE_URL_CHARS[0])
