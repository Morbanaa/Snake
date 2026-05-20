# Teddy Rodd
# Morbanaa Studios
# Snake

import time
from game_manager import Game_Manager

def main():
    game_speed = 0.5
    game_manager = Game_Manager(25,50)
    game_manager.world_gen()
    while True:
        game_manager.render_world()
        game_manager.clear_move_cursor()
        time.sleep(game_speed)

if __name__ == "__main__":
    main()
