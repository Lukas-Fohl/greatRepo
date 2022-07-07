from output import screen_renderer as screen_render_import

final_view: int = [0]

def raycasting(render_distacne_in: int,degrees_in: int,map_in: str = [[],[]]):
    #do the fun stuff
    screen_render_import.renderer(final_view)
    return

def output_nur_so(map_in: str = [[],[]]):
    for y in map_in:
        print()
        for x in y:
            print(x*2,end="")
    return