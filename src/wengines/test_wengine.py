import glob
import json
import os

PATH = "/mnt/g/projetos/Projects/Gamegacha_scraper/output/wengines/wengines_data"
FILE_NAME = "game_data_wengine"


def build_game_data(path, output_name):
    search_pattern = os.path.join(path, "*.json")

    file_names = glob.glob(search_pattern)

    output = {}
    for file_name in file_names:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            output[data["id"]] = data

    output_path = os.path.join(path + f"/{output_name}.json")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(output))


build_game_data(PATH, FILE_NAME)
