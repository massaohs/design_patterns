import json
import os

DATASHEET_PATH = os.path.join(os.getcwd(), 'esteira_v3/datasheet/datasheet.json')
MAP_PROCESS_PATH = os.path.join(os.getcwd(), 'esteira_v3/datasheet/setup.json')

class LoadFiles:

    def get_info_datasheet(self):
        file = open(DATASHEET_PATH)
        return json.load(file)

    def setup(self):
        file = open(MAP_PROCESS_PATH)
        return json.load(file)