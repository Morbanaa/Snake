import keyboard

class Player():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos
        self.direction = 1


    def update(self,game_map):
        # left
        if self.direction == 1 and game_map[self.ypos][self.xpos -1] != "@":
            self.xpos -= 1
        
        # Right
        if self.direction == 2 and game_map[self.ypos][self.xpos +1] != "@":
            self.xpos += 1

        # Up
        if self.direction == 3 and game_map[self.ypos -1][self.xpos] != "@":
            self.ypos -= 1
        
        # Down
        if self.direction == 4 and game_map[self.ypos +1][self.xpos] != "@":
            self.ypos += 1

        # Turning Up
        if keyboard.is_pressed("W"):
            self.direction = 3

        # Turning Down
        if keyboard.is_pressed("S"):
            self.direction = 4

        # Turning Left
        if keyboard.is_pressed("A"):
            self.direction = 1
        
        # Turning Right
        if keyboard.is_pressed("D"):
            self.direction = 2