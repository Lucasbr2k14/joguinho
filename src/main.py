import pygame as pg
from player import Player
from shot import Shot

class Game:


    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280, 720))
        self.runing = True
        self.clock  = pg.time.Clock()
        
        self.player = Player(self.screen)
        self.shot   = Shot(self.screen)

        self.mouse_pressed = False

        self.run()


    def loop(self):
        keys = pg.key.get_pressed()

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
            self.shot.shot(tuple(self.player.position), pg.mouse.get_pos())
            self.mouse_pressed = True


        if not pg.mouse.get_pressed()[0]:
            self.mouse_pressed = False


        self.shot.flight()
        self.shot.draw()


        self.player.mcpose()
        self.player.draw()

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