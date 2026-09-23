import logging
import sys
import traceback

from selenium import webdriver

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
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        browser = webdriver.Remote("http://172.17.0.2:4444/wd/hub", options=options)  # type: ignore
    except Exception:
        logging.error("Browser cannot be opening...")
        traceback.print_exc()


def load_page(url):
    try:
        start_session()
        logging.warning("acessando a url: %s", url)
        browser.get(url)
    except Exception:
        logging.error("url: %s", url)
        traceback.print_exc()


def browser_instance():
    return browser


def stop_session():
    try:
        browser.quit()
    except Exception:
        logging.error("Browser cannot be closing...")
        traceback.print_exc()
