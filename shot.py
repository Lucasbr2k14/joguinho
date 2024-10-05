from pygame import Surface, draw

x = 0
y = 1

class Shot:

    def __init__(self, screen:Surface):
        self.radius   = 5
        self.velocity = 4
        self.screen   = screen
        self.shots    = []

    def shot(self, player_pos:tuple, mouse_pos:tuple):

        hip_len  = pow(pow(player_pos[x] - mouse_pos[x], 2) + pow(player_pos[y] - mouse_pos[y], 2), 1/2) 

        sin = (mouse_pos[x] - player_pos[x])/hip_len
        cos = (player_pos[y] - mouse_pos[y])/hip_len
    
        self.shots.append({
            "posi": [player_pos[x], player_pos[y]],
            "x_sum": sin * self.velocity,
            "y_sum": cos * self.velocity,
        })

    def flight(self):
        if len(self.shots) > 0:
            for i in range(len(self.shots)):
                self.shots[i]["posi"][x] += self.shots[i]["x_sum"]
                self.shots[i]["posi"][y] -= self.shots[i]["y_sum"]

    def draw(self):
        if len(self.shots) > 0:
            for i in range(len(self.shots)):
                draw.circle(self.screen, 'white', self.shots[i]["posi"], self.radius)
    