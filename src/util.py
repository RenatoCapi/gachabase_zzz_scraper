import re


def float_to_int(value) -> int:
    return int(round(value, 4) * 10000)


def text_to_float(text: str):
    return float(text.rstrip("%"))


def text_to_int(text: str):
    return float_to_int(text_to_float(text))


def find_wengine_id(text):
    pattern = r"(\d{5})"
    match = re.search(pattern, text)
    if match:
        return match.group(1)

    return ""
