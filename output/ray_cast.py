from output import screen_renderer as screen_render_import
from output import output as output_import
from designe import map as map_import
import math as math_import

final_view: int = [0]
cam_pos = [0,0]
degrees_ = 0

def raycasting(render_distacne_in: int,degrees_in: int,map_in: str = [[],[]]):
    #do the fun stuff
    global cam_pos
    global  degrees_ 
    degrees_ = degrees_in
    if output_import.cam_eq_player == True:
        cam_pos = map_import.get_current_player_position()
    casting()
    screen_render_import.renderer(final_view)
    return

def casting():
    final_lenght = 0
    x_offset = 0
    y_offset = 0
    try:
        both_casting()
    except:
        return final_lenght
    return None

def both_casting():
    while get_horizontal_distance() > get_vertical_distance():
        vertical_search()
    while get_horizontal_distance() < get_vertical_distance():
        horizonal_search()
    both_casting()
    return

def vertical_search():
    #manage the casting (vertical) 
    get_vertical_distance()
    return
    
def horizonal_search():
    #manage the casting (horizontal) 
    get_horizontal_distance()
    return

def vertical(angle_in: float,x_offset:int):
    hiting =  math_import.tan(deg_2_rad(angle_in))*x_offset
    return hiting

def horizontal(angle_in: float,y_offset:int):
    new_angle = abs(90-angle_in)
    hiting = math_import.tan(deg_2_rad(new_angle))*y_offset
    return hiting

def hit_hit_stuff(orientation: int, position: float = []):
    match orientation:
        case 0:
            print()
            #vertical +1
        case 1:
            print()
            #horizontal +1
        case 2:
            print()
            #vertical -1
        case 3:
            print()
            #horizontal -1
    return

def rad_2_deg(rad:float):
    return (rad)*(180/math_import.pi)

def deg_2_rad(deg:float):
    return (deg)*(math_import.pi/180)

def orientation(angle: int):
    choice = 0
    if angle >= 0 and angle < 45:
        choice = 0
    elif angle >=45 and angle <= 135:
        choice = 1
    elif angle >= 135 and angle <= 225:
        choice = 2
    elif angle >= 225 and angle <= 315:
        choice = 3
    elif angle >=315 and angle <= 360:
        choice = 0
    return choice

def get_vertical_distance():
    vertical()
    return

def get_horizontal_distance():
    horizontal()
    return

######

def output_just_cuz(map_in: str = [[],[]]):
    for y in map_in:
        print()
        for x in y:
            print(x*2,end="")
    return
