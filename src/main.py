import pygame as pg
from player import Player
from shot import Shot
from hud import Hud

class Game:


    def __init__(self):

        pg.init()
        self.screen    = pg.display.set_mode((1280, 720))
        self.runing    = True
        self.shot_cool = 0
        self.clock     = pg.time.Clock()
        
        
        self.player = Player(self.screen) 
        self.shot   = Shot(self.screen)
        self.hud    = Hud(self.screen)
        
        
        # pg.display.toggle_fullscreen()

        self.mouse_pressed = False
        self.run()


    def loop(self):

        keys = pg.key.get_pressed()
        if self.shot_cool <= 0:
            if keys[pg.K_w]:
                self.player.walk_up()
                
            if keys[pg.K_s]:
                self.player.walk_down()

            if keys[pg.K_d]:
                self.player.walk_right()
                
            if keys[pg.K_a]:
                self.player.walk_left()
            
        if keys[pg.K_w] or keys[pg.K_s] or keys[pg.K_d] or keys[pg.K_a]:
            self.player.walking(True)
        else:
            self.player.walking(False)


        self.screen.fill("black")

        if pg.mouse.get_pressed()[0] and not self.mouse_pressed:
            if self.hud.return_mana()>=10:
                if self.shot_cool <= 0:
                    position_shot = self.player.shot()
                    self.shot.shot(position_shot, pg.mouse.get_pos())
                    self.mouse_pressed = True
                    self.shot_cool = 3
                    self.hud.new_mana()
        else:
            self.shot_cool -= 0.1


        if not pg.mouse.get_pressed()[0]:
            self.mouse_pressed = False


        self.shot.flight()
        self.shot.draw()


        self.player.mcpose()
        self.player.draw(self.shot_cool)
        self.hud.draw()
        self.hud.recharge_mana()
        pg.display.flip()
        self.clock.tick(60)


    def run(self):

        
        while self.runing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runing = False

            self.loop()

        pg.quit()

Game()
