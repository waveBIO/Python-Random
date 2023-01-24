import pygame
import main

class Player:
    def __init__(self,startKoordX,startKoordY):
        self.x = startKoordX
        self.y = startKoordY
        self.speed = 9


    #0left 1right 2up 3down
    def move(self,direction):
        if direction == 0:
            self.x -= self.speed
        if direction == 1:
            self.x += self.speed
        if direction == 2:
            self.x -= self.speed
        if direction == 3:
            self.x += self.speed


