import logging
import time
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from gachabase_webscraper import start_session
from wengines.wengine_constants import BASEDATA_XPATH, NAME_XPATH, PARAM_LIST_WENGINE

from browser_manager import load_page
from constants import URL_BASE_GACHABASE


def _get_wengine(browser, wengine_url):
    load_page(URL_BASE_GACHABASE + wengine_url)
    close_dialog(browser, "dialog:s21:close")
    close_dialog(browser, "dialog:s20:close")

    browser.quit()

    pass


def get_wengine_metadata(browser):
    core_element = browser.find_element(By.XPATH, BASEDATA_XPATH)
    wengine_name = core_element.find_elements(By.XPATH, NAME_XPATH).text

    pass


def get_wengines_url_list(browser):
    try:
        start_session()
        logging.warning("acessando a url: %s", URL_BASE_GACHABASE + PARAM_LIST_WENGINE)
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
    except Exception:
        logging.error("url: %s", URL_BASE_GACHABASE + PARAM_LIST_WENGINE)
        traceback.print_exc()
        return []


def close_dialog(browser, xpath_button):
    try:
        logging.info("tentando fechar o botão " + xpath_button)
        close_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, xpath_button))
        )

        close_button.click()
    except Exception:
        traceback.print_exc()
