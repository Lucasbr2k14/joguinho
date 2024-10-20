from pygame import Surface, draw

x = 0
y = 1

class Collision:

    def __init__(self, screen:Surface):
        
        self.screen      = screen
        self.show_hitbox = True
        self.scene       = []


    def test_player(self, player_poits:tuple) -> tuple:

        # O metodo test_player retorna a colisão do senário
        # Ela vai retornar uma tupla (Cima, Baixo, Esquerda, Direita)

        collision = [False,False,False,False]

        # Colisão com as bordas do mapa

        if player_poits[0][1] <= 0:
            collision[0] = True
        if player_poits[1][1] >= self.screen.get_height():
            collision[1] = True
        if player_poits[0][0] <= 0:
            collision[2] = True 
        if player_poits[1][0] >= self.screen.get_width():
            collision[3] = True

        # for i in range(len(1)):
        #     pass
        
        if self.show_hitbox:
            draw.line(self.screen, "red", player_poits[0], (player_poits[1][0], player_poits[0][1]), 2)
            draw.line(self.screen, "red", (player_poits[1][0], player_poits[0][1]), player_poits[1], 2)
            draw.line(self.screen, "red", player_poits[1], (player_poits[0][0], player_poits[1][1]), 2)
            draw.line(self.screen, "red", (player_poits[0][0], player_poits[1][1]), player_poits[0], 2)
            
        return tuple(collision)
    

