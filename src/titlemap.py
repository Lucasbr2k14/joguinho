from pygame import Surface, image, Rect, transform
from time import sleep


class TileMap:

    def __init__(self, screen:Surface):
        
        self.screen = screen
        self.mul    = 4
        self.len    = 16
        self.matrix = []
        self.tile   = []

        self.load_visuals()
        self.load_map()
        self.cache_tilemap()

    def load_visuals(self):
        self.visuals = image.load_extended("./Sprites/land.png")
        self.visuals = transform.scale(self.visuals, (320*self.mul,320*self.mul))

    def load_map(self):
        with open("./maps/map1.csv") as file:
            for linha in file:

                linha = linha.strip().split(",")

                for i in range(len(linha)):
                    linha[i] = int(linha[i])
                
                self.matrix.append(linha)

    def cache_tilemap(self):
        for i in range(400+1):
            tile_x = 16 * self.mul * i % 320
            tile_y = i // 20 * 16 * self.mul
            rect = ((tile_x, tile_y),(16*self.mul,16*self.mul))
            self.tile.append(rect)

    def draw(self):
        tile_size = self.len*self.mul
        for i in range(len(self.matrix) * len(self.matrix[0])):
            l = i // 20
            c = i % 20
            x = c * tile_size
            y = l * tile_size
            index_tile = self.matrix[l][c]
            self.screen.blit(self.visuals, (x, y), self.tile[index_tile])