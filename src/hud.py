from pygame import Surface,draw,image

class Hud:

    def __init__(self , surface:Surface):
        self.life:int   = 0
        self.mana:float = 0.0

        self.screen = surface
        
        self.screen = surface
        self.load_visuals()
        
    def load_visuals(self):
        self.sprites = image.load_extended("./Sprites/teste.png")
        
    def draw(self):
        draw.rect(self.screen,'red',[(0,0),(self.life,16)])
        draw.rect(self.screen,'blue',[(0,18),(self.mana,16)])
        self.screen.blit(self.sprites,[0,0],[[0,432],[101,16]])
        self.screen.blit(self.sprites,[0,18],[[0,432],[101,16]])
        
    def pull_from_player(self, player:tuple[int, float]):
        self.life = player[0]
        self.mana = player[1]