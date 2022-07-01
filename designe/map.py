import json
import os

map_2d   =[[],[]]
map_path =  os.path.dirname(os.path.abspath(__file__)) +"\main.json"
map_data = {}

def translate_map(scene_in,map_in):
    with open(map_path,"r") as json_file:
        map_data = json.load(json_file)
        map_2d = map_data[scene_in][map_in]
    return map_2d