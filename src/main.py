from gachabase_webscraper import get_char_url_list, write_all_chars
import logger_provider
from wengines.gachabase_wengines import write_all_wengines, write_wengine

logger = logger_provider.get_logger()


def main():
    # get_char_url_list()
    # write_wengine(0)
    # write_char(1)
    # write_all_chars()
    write_wengine(20)
    # write_all_wengines()
    logger.warning("concluido, terminando o script!")


if __name__ == "__main__":
    main()
