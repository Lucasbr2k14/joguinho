from pygame import Surface, draw

class Collision:

    def __init__(self, screen:Surface, show_hitbox = False):
        
        self.screen:Surface      = screen
        self.show_hitbox:bool    = show_hitbox
        self.rects_colision:list = [] 
    
    def get_collision_tilemap(self, collision:list):
        for i in range(len(collision)):
            self.rects_colision.append(collision[i])

    def test_player(self, player_poits:tuple) -> tuple:

        # O metodo test_player retorna a colisão do senário
        # Ela vai retornar uma tupla (Cima, Baixo, Esquerda, Direita)

        collision = [False,False,False,False]

        # Definindo pontos A,B,C e D do dado da colisão e do personagem  
        player_A = player_poits[0]
        player_B = (player_poits[1][0], player_poits[0][1])
        player_C = player_poits[1]
        player_D = (player_poits[0][0], player_poits[1][1])

        for i in range(len(self.rects_colision)):
            # Definindo os pontos do obejto cujo o player vai colidir
            
            rect_colision:list = self.rects_colision[i]

            object_A:tuple = rect_colision[0]
            object_B:tuple = (rect_colision[1][0], rect_colision[0][1])
            object_C:tuple = rect_colision[1]
            object_D:tuple = (rect_colision[0][0], rect_colision[1][1])

            # Verificar se player bateu na linha de baixo para cima

            if (
                (player_A[1] <= object_D[1] and player_A[1]+5 >= object_C[1]) and 
                (player_A[0] >= object_D[0] and player_A[0]   <= object_C[0]) or
                (player_B[1] <= object_D[1] and player_B[1]+5 >= object_C[1]) and 
                (player_B[0] >= object_D[0] and player_B[0]   <= object_C[0]) 
            ):
                collision[0] = True

            # Verificar se o player bateu na linha de cima para baixo

            if (
                (player_C[1] >= object_A[1] and player_C[1]-5 <= object_B[1]) and
                (player_C[0] >= object_A[0] and player_C[0]   <= object_B[0]) or
                (player_D[1] >= object_A[1] and player_D[1]-5 <= object_B[1]) and
                (player_D[0] >= object_A[0] and player_D[0]   <= object_B[0])
            ):
                collision[1] = True

            # Verificando da esquerda para a direita

            if (
                (player_A[0] >= object_B[0] and player_A[0] <= object_C[0]+5) and
                (player_A[1] >= object_B[1] and player_A[1] <= object_C[1]  ) or
                (player_D[0] >= object_B[0] and player_D[0] <= object_C[0]+5) and
                (player_D[1] >= object_B[1] and player_D[1] <= object_C[1]  )
            ):
                collision[2] = True


            # Verificando da direita para esquerda

            if (
                (player_B[0] >= object_A[0] and player_B[0] <= object_D[0]+5) and
                (player_B[1] >= object_A[1] and player_B[1] <= object_D[1]  ) or
                (player_C[0] >= object_A[0] and player_C[0] <= object_D[0]+5) and
                (player_C[1] >= object_A[1] and player_C[1] <= object_D[1]  )
            ):
                collision[3] = True

        # Colisão com as bordas do mapa

        if player_poits[0][1] <= 0:
            collision[0] = True

        if player_poits[1][1] >= self.screen.get_height():
            collision[1] = True
        if player_poits[0][0] <= 0:
            collision[2] = True 
        if player_poits[1][0] >= self.screen.get_width():
            collision[3] = True

        if self.show_hitbox:
            draw.line(self.screen, "red", player_A, player_B, 2)
            draw.line(self.screen, "red", player_B, player_C, 2)
            draw.line(self.screen, "red", player_C, player_D, 2)
            draw.line(self.screen, "red", player_D, player_A, 2)
        
        return tuple(collision)

    def draw_hitbox(self):
        if self.show_hitbox:
            for i in range(len(self.rects_colision)):
                cenario = self.rects_colision[i]
                draw.line(self.screen, "red", cenario[0], (cenario[1][0], cenario[0][1]), 2)
                draw.line(self.screen, "red", (cenario[1][0], cenario[0][1]), cenario[1], 2)
                draw.line(self.screen, "red", cenario[1], (cenario[0][0], cenario[1][1]), 2)
                draw.line(self.screen, "red", (cenario[0][0], cenario[1][1]), cenario[0], 2)
            