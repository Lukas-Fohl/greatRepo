from output import screen_renderer as screen_render_import
from output import output as output_import
from designe import map as map_import
import math as math_import

final_view: int = [0]
cam_pos = [0,0]

def raycasting(render_distacne_in: int,degrees_in: int,map_in: str = [[],[]]):
    #do the fun stuff
    global cam_pos
    if output_import.cam_eq_player == True:
        cam_pos = map_import.get_current_player_position()
    screen_render_import.renderer(final_view)
    return

def casting():
    x_offset = 0
    y_offset = 0
    return None

def vertical(angle_in: float,x_offset:int):
    hiting =  math_import.tan(deg_2_rad(angle_in))*x_offset
    return hiting

def horizontal(angle_in: float,y_offset:int):
    new_angle = abs(90-angle_in)
    hiting = math_import.tan(deg_2_rad(new_angle))*y_offset
    return hiting

def hit_hit_stuff(orientation: int, position: float = []):
    return

def rad_2_deg(rad:float):
    return (rad)*(180/math_import.pi)

def deg_2_rad(deg:float):
    return (deg)*(math_import.pi/180)

def orientation(angle: int):
    choice = 0
    if angle >= 0:
        choice = 0
    elif angle >= 90:
        choice = 0
    elif angle >= 180:
        choice = 0
    elif angle >= 270:
        choice = 0
    return choice

def output_just_cuz(map_in: str = [[],[]]):
    for y in map_in:
        print()
        for x in y:
            print(x*2,end="")
    return
