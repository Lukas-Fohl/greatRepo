from game_logic import main_logic as main_logic_import
from designe import map as map_import
from output import output as output_import
from logic import collision as collision_import

def main():
    main_logic_import.main_logic()
    output_import.output_manager(False)
    ent_listing = [main_logic_import.main_player.entity, main_logic_import.main_player.entity]
    collision_import.multi_collision(ent_listing)
    return

if __name__ == "__main__":
    main()