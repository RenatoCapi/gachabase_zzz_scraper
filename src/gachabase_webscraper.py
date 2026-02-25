import json
import logging
import os
import re
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests

from constants import *
from xpath_constants import *
from xpath_constants import get_skill_xpath

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


logging.info("abrindo o browser...")
options = webdriver.ChromeOptions() # type: ignore
options.add_argument("--headless")
browser = webdriver.Remote("http://172.17.0.2:4444/wd/hub", options=options) # type: ignore

browser.maximize_window()

hit_map_aux = {}

def _get_char_url(char_url:str) -> str:
    return f"{URL_BASE_GACHABASE}/{char_url}"

def _get_char_skillkit(param_char_url):
    skillkit = {}
    browser.get(URL_BASE_GACHABASE + param_char_url)

    logging.info(f"acessando: '{URL_BASE_GACHABASE + param_char_url}'")

    #fechar o dialog
    close_button = browser.find_element(By.XPATH, XPATH_CLOSE_BUTTON)
    action = ActionChains(browser)
    action.click(close_button).perform()

    hit_map_aux = {}
    for skill_id in range(1,6):
        logging.info(GAMEGACHA_SKILLS_SECTION_MAP[skill_id])
        skillkit[GAMEGACHA_SKILL_MAP[skill_id]] = _get_skill_data(skill_id)

    return {
        'skillKit': skillkit,
        'hitMap': hit_map_aux
    }


def _get_skill_data(skill_id:int):
    element_skills = browser.find_element(By.XPATH, XPATH_BASE_GAMEGACHA_SKILLS + get_skill_xpath(skill_id))
    elements_desc = element_skills.find_element(By.XPATH, XPATH_SKILL_DESCS)

    desc = []

    logging.info(f'pegando desc...')
    for element_desc in elements_desc.find_elements(By.CLASS_NAME,"text-sm "):
        element_html = element_desc.get_attribute("outerHTML")
        desc.append(str(BeautifulSoup(element_html,'html.parser')))

    return {
        "skillId":skill_id,
        "desc":desc,
        "subSkills": _get_sub_skills_data(skill_id, element_skills)
    }


def _get_sub_skills_data(skill_id:int, element_skills):
    sub_skills_data = element_skills.find_elements(By.XPATH, XPATH_SUB_SKILLS_DATA)
    sub_skills = {}
    sub_skill_id = ""

    for id, sub_skill_data in enumerate(sub_skills_data):
        if id & 1 == 0:
            sub_skill_id = sub_skill_data.find_element(By.XPATH,"./h3").text
            slider = sub_skill_data.find_element(By.XPATH, XPATH_SLIDER_SUB_SKILLS)
            logging.info(f'pegando {sub_skill_id}...')
        else:
            sub_skills[sub_skill_id] = lvl_skill_slider_manager(sub_skill_data, sub_skill_id, slider)
    
    return sub_skills


def lvl_skill_slider_manager(sub_skill_data, sub_skill_id, slider):
    logging.info(f'iniciando manipulação do slider...')

    action = ActionChains(browser)
    action.click_and_hold(slider).move_by_offset(-20*17,0).release().perform()
    sub_skill = {}

    for count in range(1,17):
        print(slider.get_attribute("aria-valuenow"))
        tables_element = sub_skill_data.find_elements(By.TAG_NAME,'tbody')
        sub_skill = _get_complex_hits_data(tables_element[0], sub_skill_id, sub_skill)
        _update_hit_map(tables_element[1])
        action.click_and_hold(slider).move_by_offset(19,0).release().perform()


    return sub_skill


def _get_complex_hits_data(tbody_element,sub_skill_id, sub_skill):
    logging.info(f'construindo a subSkill...')
    tr_elements = tbody_element.find_elements(By.TAG_NAME,'tr')
    
    for tr in tr_elements:
        complex_hit_id = ""
        html_tr = tr.get_attribute('outerHTML')
        tds_soup = BeautifulSoup(html_tr, 'html.parser').find_all('td')
        spans_name_soup = tds_soup[0].find_all('span')

        if len(spans_name_soup) < 2:
            continue

        raw_name = find_hit_complex_id(spans_name_soup[0].get_text(strip=True)) # type: ignore
        raw_ids = spans_name_soup[1].get_text(strip=True).split(', ')
        multiplier = tds_soup[1].contents[2].span.get_text(strip=True) # type: ignore

        if not raw_name[1]:
            continue

        if not raw_name[0]:
            complex_hit_id = sub_skill_id
        else:
            complex_hit_id = raw_name[0] + raw_name[2]

        if complex_hit_id in sub_skill:
            sub_skill[complex_hit_id][raw_name[1].lower()].append(multiplier)

        else:
            sub_skill[complex_hit_id] = {
                    "hitID": raw_ids,
                    "dmg": [],
                    "daze": []
                }
            
            sub_skill[complex_hit_id][raw_name[1].lower()].append(multiplier)

    return sub_skill


def find_hit_complex_id(raw:str) -> tuple:
    pattern = r'^(.*?)\s*(DMG|Daze)\sMultiplier(.*)$'
    match = re.search(pattern, raw)
    if match:
        return match.groups()
    
    return ("","","")


def _update_hit_map(tbody_element):
     tr_elements = tbody_element.find_elements(By.TAG_NAME,'tr')
     for tr in tr_elements:
        html_tr = tr.get_attribute('outerHTML')
        th_soup = BeautifulSoup(html_tr, 'html.parser').find('th')
        tds_soup = BeautifulSoup(html_tr, 'html.parser').find_all('td')
        simple_hit_id =  th_soup.get_text(strip=True) # type: ignore

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


def selenium_test():
    try:
        char = _get_char_skillkit(GACHABASE_URL_CHARS[0])
        folder_path = '/app/output'
        file_name = f"{CHAR_ID_LIST[0]}.json"
        complete_path = os.path.join(folder_path, file_name)

        logging.info(f'escrevendo no caminho {complete_path}')

        with open(complete_path, "w") as file:
            file.write(json.dumps(char))
        
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc() 

    finally:
        browser.quit()


#usado uma vez pra pegar o mapa de urls
def _get_char_url_list():
    content = _request_html_content(URL_BASE_GACHABASE + PARAM_LIST_AGENTS)
    soup = BeautifulSoup(content)
    links_list_soup = soup.find('div', id="entries").find_all('a')  # type: ignore
    char_url_list = []
    for url_char in links_list_soup:
        char_url_list.append(url_char['href']) # type: ignore

    return char_url_list


def _request_html_content(url: str):
    resp = requests.get(url, headers=HEADERS, timeout=5)
    return resp.content


if __name__ == "__main__":
    selenium_test()