import pygame as pg
from player import Player
from shot import Shot

class Game:


    def __init__(self):

        pg.init()
        self.screen    = pg.display.set_mode((1280, 720))
        self.runing    = True
        self.shot_cool = 0
        self.clock     = pg.time.Clock()
        self.time      = 0 
        
        self.player = Player(self.screen) # Porque passar o cooldawn para o player?
        self.shot   = Shot(self.screen)
        
        
        # pg.display.toggle_fullscreen()

        self.mouse_pressed = False
        self.run()

    def loop(self):

        cooldown_shot = self.shot.get_cooldown(self.time)

        keys = pg.key.get_pressed()
        if self.shot_cool <= 0:
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

        self.screen.fill("black")

        if pg.mouse.get_pressed()[0] and not self.mouse_pressed:
            if self.shot.get_cooldown(self.time):
                position_shot = self.player.shot()
                self.shot.shot(position_shot, pg.mouse.get_pos(), self.time)
                self.mouse_pressed = True

        if not pg.mouse.get_pressed()[0]:
            self.mouse_pressed = False

        self.shot.flight()
        self.shot.draw()

        self.player.mcpose()
        self.player.draw(self.shot.get_cooldown(self.time))


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

# Cooldawn do tiro tem que pertencer a classe do shot não a classe game.
