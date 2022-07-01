from game_logic import main_logic as main_logic_import
from designe import map as map_import
from output import output as output_import

def main():
    main_logic_import.main_logic()
    output_import.output_manager(False)
    return

if __name__ == "__main__":
    main()