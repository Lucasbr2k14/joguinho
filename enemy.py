from pygame import image,Surface
# from player import Player
import random


#screen = 1280x720
#seperar niveis de inimgos para "Enemy Vector"
class SelectEnemy:
    def __init__(self, screen:Surface):
        
        self.screen = screen
        self.level = 1
        
        self.spawnPoints = [[random.randrange(1281,1289),random.randrange(-721,723)],
                       [random.randrange(-1289,-1281),random.randrange(-721,722)],
                       [random.randrange(-1281,1282),random.randrange(-730,-721)],
                       [random.randrange(-1281,1282),random.randrange(721,730)]
        ]

        print(self.spawnPoints[0])


        self.Slime = Slime(self.screen,self.spawnPoints[0])

        self.enemyVector = [self.Slime.draw(self.spawnPoints[0])] #Colocar aqui outros imigos
    
    def enemySelector(self, playerPosition): 
        for i in range(random.randrange(0,5*self.level)):
            self.walkingEnemy(playerPosition,self.enemyVector[random.randrange(0,self.level)])
    
    
    def walkingEnemy(self, playerPosition, enemy):
        self.Slime.follow_player(playerPosition)
        self.Slime.draw(self.Slime.pos)

class Slime:
    def __init__(self, screen:Surface, pos:tuple):
        self.screen = screen
        self.speed  = 1
        self.load_image()
        self.pos = pos

    def load_image(self):
        self.sprites = image.load_extended("./Sprites/teste.png")
        
    def draw(self, position:tuple):
        self.screen.blit(self.sprites, self.pos,[[0,128],[16,16]])
        
    def follow_player(self, player_pos:tuple):
        if self.pos[0]+8<player_pos[0]:
            self.pos[0]+=self.speed
        elif self.pos[0]+8>=player_pos[0]:
            self.pos[0]-=self.speed
        if self.pos[1]+13<player_pos[1]:
            self.pos[1]+=self.speed
        elif self.pos[1]+13>=player_pos[1]:
            self.pos[1]-=self.speed