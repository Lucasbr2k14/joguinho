import pygame as pg
from player import Player
from shot import Shot
from hud import Hud
from titlemap import TileMap

class Game:


    def __init__(self):

        pg.init()
        self.screen    = pg.display.set_mode((1280, 720))
        self.runing    = True
        self.shot_cool = 0
        self.clock     = pg.time.Clock()
        self.time      = 0 
        
        
        self.player  = Player(self.screen)
        self.shot    = Shot(self.screen)
        self.hud     = Hud(self.screen)
        self.titlemap= TileMap(self.screen) 
        
        # pg.display.toggle_fullscreen()

        self.mouse_pressed = False
        self.run()

    def loop(self):

        
        # self.screen.fill("black")

        cooldown_shot = self.shot.get_cooldown()

        keys = pg.key.get_pressed()

        if self.shot.cooldown <= 0:
            if keys[pg.K_w]:
                self.player.walk_up(cooldown_shot)
                
            if keys[pg.K_s]:
                self.player.walk_down(cooldown_shot)

            if keys[pg.K_d]:
                self.player.walk_right(cooldown_shot)
                
            if keys[pg.K_a]:
                self.player.walk_left(cooldown_shot)
            
        if keys[pg.K_w] or keys[pg.K_s] or keys[pg.K_d] or keys[pg.K_a]:
            self.player.walking(True)
        else:
            self.player.walking(False)

        if pg.mouse.get_pressed()[0] and not self.mouse_pressed:
            if self.hud.return_mana() >= 10:
                if self.shot.cooldown <= 0:
                    position_shot = self.player.shot()
                    self.shot.shot(position_shot, pg.mouse.get_pos(), self.time)
                    self.mouse_pressed = True
                    self.shot.cooldown = 3
                    self.hud.new_mana()
        else:
            self.shot.cooldown -= 0.1


        if not pg.mouse.get_pressed()[0]:
            self.mouse_pressed = False




        self.shot.flight()
        
        self.player.mcpose()
        self.hud.recharge_mana()


        self.titlemap.draw()
        self.shot.draw()
        self.player.draw(cooldown_shot, self.shot.cooldown)
        self.hud.draw()

        pg.display.flip()

        self.time += self.clock.tick(60)
        

    def run(self):

        
        while self.runing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runing = False

            self.loop()

        pg.quit()

Game()