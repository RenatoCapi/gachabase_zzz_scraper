import logging
import glob
import json
import os
import traceback

from util import text_to_int

logging.basicConfig(
    filename="/mnt/g/projetos/Projects/Gamegacha_scraper/output/app.log",
    encoding="utf-8",
    filemode="a",  # 'a' means append
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ("daze":) \[\n[\S\s]*?\]


def fix_all_chars_formulas():
    search_pattern = os.path.join(
        "/mnt/g/projetos/Projects/Gamegacha_scraper/output/tests", "*.json"
    )

    # Use glob to find all files matching the pattern
    file_names = glob.glob(search_pattern)

    for file_name in file_names:
        with open(file_name, "r+", encoding="utf-8") as f:
            try:
                logging.info(file_name)
                data = json.load(f)
                data_permutation(data)
                f.seek(0)
                f.write(json.dumps(data))
                f.truncate()
                logging.info("arquivo atualizado")
            except json.JSONDecodeError:
                logging.info(f"Error decoding JSON from file: {file_name}")
            except Exception as e:
                logging.info(f"An unexpected error occurred with file {file_name}: {e}")
                traceback.print_exc()

        # break


def data_permutation(data):
    hit_map = data["hitMap"]
    logging.info(data["name"])
    for skill_id, skill in data["skillKit"].items():
        logging.info(skill_id)
        for sub_skill_id, sub_skill in skill["subSkills"].items():
            logging.info(sub_skill_id)
            for hit_id, complex_hit in sub_skill.items():
                logging.info(hit_id)
                fix_formula(hit_id, complex_hit, hit_map)


def fix_formula(complex_hit_id: str, complex_hit: dict, hit_map):
    # casos
    # 1 id e a conversão de lvl 1 bate
    # 1 id mas os números não batem
    # mais de 1 id

    if isinstance(complex_hit["dmg"], dict) and isinstance(complex_hit["daze"], dict):
        return

    if len(complex_hit["hitID"]) == 1:
        if isinstance(complex_hit["dmg"], list) and len(complex_hit["dmg"]) == 2:
            compare_hit_map_data(complex_hit, hit_map[complex_hit["hitID"][0]], "dmg")
        if isinstance(complex_hit["daze"], list) and len(complex_hit["daze"]) == 2:
            compare_hit_map_data(complex_hit, hit_map[complex_hit["hitID"][0]], "daze")
    elif len(complex_hit["hitID"]) > 1:
        compare_calc_mult_sum(complex_hit, hit_map)
    else:
        logging.info("erro inexperado!!!")

    if len(complex_hit["dmg"]) == 0:
        complex_hit["dmg"] = {"base": 0, "growth": 0}

    if len(complex_hit["daze"]) == 0:
        complex_hit["daze"] = {"base": 0, "growth": 0}


def compare_hit_map_data(complex_hit, simple_hit, mult_id):
    mult_aux = str_multiplier(complex_hit[mult_id][0], complex_hit[mult_id][1])

    if mult_aux["base"] == -1:
        complex_hit[mult_id] = simple_hit
        complex_hit["formula"] = "{" + complex_hit["hitID"][0] + "}"
        return

    if (
        mult_aux["base"] == simple_hit[mult_id]["base"]
        and mult_aux["growth"] == simple_hit[mult_id]["growth"]
    ):
        complex_hit[mult_id] = mult_aux
        complex_hit["formula"] = "{" + complex_hit["hitID"][0] + "}"
        return

    greater_div, greater_mod = divmod(
        (mult_aux["base"] + mult_aux["growth"] * 16),
        (simple_hit[mult_id]["base"] + simple_hit[mult_id]["growth"] * 16),
    )

    if greater_mod == 0:
        complex_hit[mult_id] = simple_hit
        complex_hit["formula"] = (
            "{" + complex_hit["hitID"][0] + "}" + "*" + str(greater_div)
        )
        return

    less_div, less_mod = divmod(
        (simple_hit[mult_id]["base"] + simple_hit[mult_id]["growth"] * 16),
        (mult_aux["base"] + mult_aux["growth"] * 16),
    )

    if less_mod == 0:
        complex_hit[mult_id] = simple_hit
        complex_hit["formula"] = (
            "{" + complex_hit["hitID"][0] + "}" + "/" + str(less_div)
        )
        return

    logging.info("formula não identificada!!!")


def compare_calc_mult_sum(complex_hit, hit_map):
    hit_dmg_aux = {"base": 0, "growth": 0}
    hit_daze_aux = {"base": 0, "growth": 0}

    formula = ""
    for hit_id in complex_hit["hitID"]:
        formula += "{"
        hit_dmg_aux["base"] += hit_map[hit_id]["dmg"]["base"]
        hit_dmg_aux["growth"] += hit_map[hit_id]["dmg"]["growth"]
        hit_daze_aux["base"] += hit_map[hit_id]["daze"]["base"]
        hit_daze_aux["growth"] += hit_map[hit_id]["daze"]["growth"]
        formula += hit_id + "}+"

    formula = formula[:-1]

    print(complex_hit)
    complex_calc_dmg = str_multiplier(complex_hit["dmg"][0], complex_hit["dmg"][1])

    if (
        complex_calc_dmg["base"] == hit_dmg_aux["base"]
        or complex_calc_dmg["base"] == -1
    ):
        complex_hit["dmg"] = hit_dmg_aux
        complex_hit["daze"] = hit_daze_aux
        complex_hit["formula"] = formula
    else:
        logging.warning("não é uma somátoria!!!")


def str_multiplier(lvl1_str, lvl16_str) -> dict[str, int]:
    try:
        lvl1 = text_to_int(lvl1_str)
        lvl16 = text_to_int(lvl16_str)
        growth = int((lvl16 - lvl1) / 15)

        return {"base": lvl1, "growth": growth}
    except (ValueError, TypeError):
        logging.info("não foi possível converter")
        return {"base": -1, "growth": -1}


if __name__ == "__main__":
    fix_all_chars_formulas()
