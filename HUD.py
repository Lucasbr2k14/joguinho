from pygame import Surface,draw
class HUD:
    def __init__(self,surface:Surface):
        self.mana=100
        self.vida=50
        self.surface=surface
    def draw(self):
        draw.rect(self.surface,'blue',[(0,0),(self.mana,20)])
        
    def new_mana(self):
        self.mana-=10