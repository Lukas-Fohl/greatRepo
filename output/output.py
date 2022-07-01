from designe import map as map_import
from output import ray_cast as ray_cast_import
from scene import scenemanager as scene_manager_import
import json
import os 

config_path = ""
path_contain = os.path.dirname(os.path.abspath(__file__)) 

game_map_now = [[],[]]
scene_chosen = ""
map_chosen = ""
cam_eq_player = True
frame_rate = 30

def output_manager(custom):
    get_json_config()
    frame_rate_set()
    if (custom == False):
        initi()
    global game_map_now
    game_map_now = map_import.translate_map(scene_chosen,map_chosen)
    return

def initi():
    global scene_chosen
    global map_chosen
    global cam_eq_player
    scene_chosen = scene_manager_import.scene_now
    map_chosen = scene_manager_import.map_now
    cam_eq_player = True
    return

def get_json_config():
    global config_path 
    for x in range(len(path_contain.split("\\"))-1):
        config_path += path_contain.split("\\")[x] + "\\"
    config_path += "config.json"
    return

def frame_rate_set():
    with open(config_path,"r") as json_file:
        global frame_rate
        frame_rate = json.load(json_file)['frame_rate']
    return