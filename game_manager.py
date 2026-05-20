# Teddy Rodd
# Morbanaa Studios
# Snake

import sys

class Game_Manager():
    def __init__(self,game_height,game_width):
        self.game_height = game_height
        self.game_width = game_width
        self.game_map = []

    def world_gen(self):
        for y in range (self.game_height):
            row =[]
            for x in range(self.game_width):
                if y == 0 or y == self.game_height -1 or x == 0 or x == self.game_width -1:
                    row.append("@")
                else:
                    row.append(" ")
            self.game_map.append(row)

    def render_world(self):
        for y in range(self.game_height):
            for x in range(self.game_width):
                print(f"{self.game_map[y][x]}",end="")
            print()

    def clear_move_cursor(self):
        sys.stdout.write("\033[H")
        sys.stdout.flush()