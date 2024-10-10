from pygame import Surface, image, Rect, transform

class TileMap:

    def __init__(self, screen:Surface):
        self.screen = screen

        self.mul    = 4
        self.len    = 16
        self.matrix = []
    
        self.load_visuals()
        self.load_map()


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
    
    def draw(self):
    
        for l in range(len(self.matrix)):
            for c in range(len(self.matrix[l])):

                tile_x = ((0*self.mul)+(16*self.mul)*self.matrix[l][c]) % 320
                tile_y = 0*self.mul + (self.matrix[l][c]//20)*(16*self.mul)

                rect = Rect((tile_x, tile_y),(16*self.mul,16*self.mul))
                self.screen.blit(self.visuals, (c*self.len*self.mul, (l*self.len*self.mul)), rect)