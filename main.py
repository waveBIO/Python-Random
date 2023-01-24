import pygame

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

playerOne = Player(0,0)

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Test Game - Copyright Alex S. - 2022')
fps = 60
clock = pygame.time.Clock()
bgImage = '../SCHULE/game/Assets/background.png'
backgroundImage = pygame.image.load(bgImage)
backgroundImage = pygame.transform.scale(bgImage, (800, 600))
playerImage = '../SCHULE/game/Assets/ship.png'
playerImage1 = pygame.image.load(playerImage)
def draw():
    screen.blit(playerImage1, (300,200))

def loop():
    while True:
        keys = pygame.key.get_pressed()
        clock.tick(fps)
        screen.blit(backgroundImage, (0,0))
        draw()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if keys[pygame.K_LEFT]:
                    playerOne.move(0)
                if keys[pygame.K_RIGHT]:
                    playerOne.move(1)
                if keys[pygame.K_UP]:
                    playerOne.move(2)
                if keys[pygame.K_DOWN]:
                    playerOne.move(3)

        pygame.display.flip()


if __name__ == '__main__':
    loop()