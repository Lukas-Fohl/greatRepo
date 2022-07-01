from scene import scenemanager as scene_import
from entity import player as palyer

def main_logic():
    #scene_import.load_scen(1)
    global main_player
    main_player = palyer.player 
    main_player.entity.initialize()
    main_player.entity.rotation = 0
    main_player.entity.position[0] =  0 #x
    main_player.entity.position[1] =  0 #y
    main_player.entity.destroy()

    return