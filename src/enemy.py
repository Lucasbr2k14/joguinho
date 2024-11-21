from pygame import image, Surface
from sprites.slime import Slime
import random

class SelectEnemy:
    def __init__(self, screen:Surface):
        
        self.screen = screen
        self.level = 1
        
        self.spawnPoints = [
            [random.randrange(1281,1289),random.randrange(-721,723)],
            [random.randrange(-1289,-1281),random.randrange(-721,722)],
            [random.randrange(-1281,1282),random.randrange(-730,-721)],
            [random.randrange(-1281,1282),random.randrange(721,730)]
        ]

        print(self.spawnPoints[0])


        self.Slime = Slime(self.screen, [100,100])# self.spawnPoints[0])

        self.enemyVector = [self.Slime.draw(self.spawnPoints[0])] #Colocar aqui outros imigos
    
    def enemySelector(self, playerPosition): 
        for i in range(random.randrange(0,5*self.level)):
            self.walkingEnemy(playerPosition,self.enemyVector[random.randrange(0,self.level)])
    
    
    def walkingEnemy(self, playerPosition, enemy):
        self.Slime.follow_player(playerPosition)
        self.Slime.draw(self.Slime.position)
