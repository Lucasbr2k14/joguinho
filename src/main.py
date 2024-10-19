import pygame as pg
from player import Player
from shot import Shot
from hud import Hud
from titlemap import TileMap
from collision import Collision
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
        self.collision = Collision(self.screen)


        # pg.display.toggle_fullscreen()

        self.mouse_pressed = False
        self.run()

    def loop(self):

        
        # self.screen.fill("black")


        cooldown_shot = self.shot.get_cooldown()

        keys = pg.key.get_pressed()

        self.player.walking(False)
        if self.shot.cooldown <= 0:
            if keys[pg.K_w]:
                if not keys[pg.K_s]:
                    self.player.walk_up(cooldown_shot)
                    self.player.walking(True)
                
            if keys[pg.K_s]:
                if not keys[pg.K_w]:
                    self.player.walk_down(cooldown_shot)
                    self.player.walking(True)

            if keys[pg.K_d]:  
                if not keys[pg.K_a]:
                    self.player.walk_right(cooldown_shot)
                    self.player.walking(True)
                
            if keys[pg.K_a]:
                if not keys[pg.K_d]:
                    self.player.walk_left(cooldown_shot)
                    self.player.walking(True)

            if ((keys[pg.K_w] or keys[pg.K_s]) and keys[pg.K_a]) or ((keys[pg.K_w] or keys[pg.K_s]) and keys[pg.K_d]):
                self.player.velocity = 1.5
            else:
                self.player.velocity = 2


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


        self.titlemap.draw()


        self.shot.flight()
        self.shot.draw()

        print(f"{self.player.position}",end="\r")

        self.player.draw(self.shot.cooldown)
        self.hud.draw()

        self.hud.recharge_mana()

        self.collision.test_player(self.player.get_hitbox())
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