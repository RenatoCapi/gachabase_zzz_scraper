from constants import GACHABASE_URL_CHARS
from gachabase_webscraper import _get_char_skillkit


def main():
    _get_char_skillkit(GACHABASE_URL_CHARS[0])

if __name__ == "__main__":
    main()
