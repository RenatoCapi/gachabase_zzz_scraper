import logging

from gachabase_webscraper import get_char_url_list, write_all_chars
from wengines.gachabase_wengines import write_all_wengines

logging.basicConfig(
    filename="/mnt/g/projetos/Projects/Gamegacha_scraper/output/wengines/app.log",
    encoding="utf-8",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    # get_char_url_list()
    # write_wengine(0)
    write_all_wengines()
    # write_char(1)
    # write_all_chars()


if __name__ == "__main__":
    main()
