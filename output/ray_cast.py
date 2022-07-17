from output import screen_renderer as screen_render_import
from output import output as output_import
from designe import map as map_import
import math as math_import

final_view: int = [0]
cam_pos = [0,0]
degrees_ = 0
map_search = [[],[]]
final_lenght = 0
x_offset = 1
y_offset = 1

def raycasting(render_distacne_in: int,degrees_in: int,map_in: str = [[],[]]):
    #do the fun stuff
    global cam_pos
    global  degrees_ 
    global map_search
    map_search =  map_in
    degrees_ = degrees_in
    if output_import.cam_eq_player == True:
        cam_pos = map_import.get_current_player_position()
    casting()
    screen_render_import.renderer(final_view)
    return

def casting():
    global final_lenght
    try:
        both_casting()
    except:
        #print(final_lenght)
        return final_lenght
    return None

def both_casting():
    global final_lenght
    #change offset
    while get_horizontal_distance() > get_vertical_distance():
        #vertical_search()
        final_lenght = get_vertical_distance()
        x_offset += 1
    while get_horizontal_distance() < get_vertical_distance():
        #horizonal_search()
        final_lenght = get_horizontal_distance()
        y_offset += 1
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

def vertical(angle_in: float):
    hiting =  math_import.tan(deg_2_rad(angle_in))*x_offset
    return hiting

def horizontal(angle_in: float):
    new_angle = abs(90-angle_in)
    hiting = math_import.tan(deg_2_rad(new_angle))*y_offset
    return hiting

def hit_hit_stuff(orientation: int, position_in: float = []):
    new_x_position = 0
    new_y_position = 0
    match orientation:
        case 0:
            #vertical +1
            new_x_position = position_in[0]+1
            new_y_position = position_in[1]
        case 1:
            #horizontal +1
            new_x_position = position_in[0]
            new_y_position = position_in[1]+1
        case 2:
            #vertical -1
            new_x_position = position_in[0]-1
            new_y_position = position_in[1]
        case 3:
            #horizontal -1
            new_x_position = position_in[0]
            new_y_position = position_in[1]-1
    if map_search[new_x_position][new_y_position] != "0" and map_search[new_x_position][new_y_position] != "7":
        return True
    return False

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
    resu = math_import.sqrt(x_offset**2+vertical(degrees_)**2)
    return resu 

def get_horizontal_distance():
    resu = math_import.sqrt(y_offset**2+horizontal(degrees_)**2)
    return resu

######
#TODO 
#change offet some how
#manage final length
#manage shit
######

def output_just_cuz(map_in: str = [[],[]]):
    for y in map_in:
        print()
        for x in y:
            print(x*2,end="")
    return
