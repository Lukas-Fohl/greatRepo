from designe import map as map_import
from output import ray_cast as ray_cast_import
from scene import scenemanager as scene_manager_import
import json
import os 

config_path = ""
path_contain = os.path.dirname(os.path.abspath(__file__)) 

game_map_now = [[],[]]
game_map = [[],[]]
scene_chosen = ""
map_chosen = ""
cam_eq_player = True
frame_rate = 30
ray_amount = 100
fov = 90

def set_up(custom):
    get_json_config()
    values_set()
    if (custom == False):
        initi()
    global game_map_now
    game_map_now = map_import.translate_map(scene_chosen,map_chosen)
    return

def output_manager(custom):
    #
    ray_cast_import.test(map_import.get_current_map())
    #
    #run game
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
    config_path = " "
    for x in range(len(path_contain.split("\\"))-1):
        config_path += path_contain.split("\\")[x] + "\\"
    config_path += "config.json"
    config_path = config_path[1:]
    return

def values_set():
    with open(config_path,"r") as json_file:
        global frame_rate
        global ray_amount
        global fov
        data_in = json.load(json_file)
        frame_rate = data_in['frame_rate']
        ray_amount = data_in['ray_cast_amount']
        fov = data_in['fov']
    return