import logging
import sys
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def start_session():
    global browser

    try:
        logging.info("abrindo o browser...")
        options = webdriver.ChromeOptions()  # pyright: ignore[reportCallIssue]
        options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless=new")
        options.page_load_strategy = "eager"
        browser = webdriver.Remote("http://172.17.0.2:4444/wd/hub", options=options)  # type: ignore
    except Exception:
        logging.error("Browser não pode ser aberto...")
        traceback.print_exc()


def click_on_button(element):
    try:
        logging.info("tentando clicar no botão %s", element)
        ActionChains(browser).click(element).perform()
    except Exception:
        traceback.print_exc()


def load_page(url):
    try:
        start_session()
        logging.warning("acessando a url: %s", url)
        browser.implicitly_wait(5)
        browser.get(url)
    except Exception:
        logging.error("url: %s", url)
        traceback.print_exc()

    return browser


def browser_instance():
    return browser


def stop_session():
    try:
        browser.quit()
    except Exception:
        logging.error("Browser não pode ser fechado...")
        traceback.print_exc()
