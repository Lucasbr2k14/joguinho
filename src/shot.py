from pygame import Surface, draw

x = 0
y = 1

class Shot:

    def __init__(self, screen:Surface):
        
        self.radius   = 5
        self.velocity = 4
        self.screen   = screen
        self.shots    = []
        
        self.cooldown_time = 0
        self.next_shot     = 0

    def shot(self, player_pos:tuple, mouse_pos:tuple, time: int):


        if self.next_shot <= time:
        
            self.next_shot = time + self.cooldown_time

            vec_len = pow((player_pos[x] - mouse_pos[x])**2 + (player_pos[y] - mouse_pos[y])**2, 1/2)

            sin = (mouse_pos[x] - player_pos[x]) / vec_len
            cos = (player_pos[y] - mouse_pos[y]) / vec_len

            self.shots.append({
                "posi": [player_pos[x], player_pos[y]],
                "x_sum": sin * self.velocity,
                "y_sum": cos * self.velocity,
                "color": self.color
            })


    def check_condidion_of_existence(self):

        for i in range(len(self.shots) - 1, -1, -1):
            
            condition = (
                self.shots[i]["posi"][y] > 0 and 
                self.shots[i]["posi"][y] < self.screen.get_height() and 
                self.shots[i]["posi"][x] > 0 and 
                self.shots[i]["posi"][x] < self.screen.get_width()
            )
            
            if not condition:
                self.destroy(i)


    def destroy(self, shot:int):
       self.shots.pop(shot) 

    def get_cooldown(self, time:int):
        return self.next_shot <= time
    
    def flight(self):
                
        if len(self.shots) > 0:
            
            self.check_condidion_of_existence()
            
            for i in range(len(self.shots)):
                self.shots[i]["posi"][x] += self.shots[i]["x_sum"]
                self.shots[i]["posi"][y] -= self.shots[i]["y_sum"]

    def draw(self):

        if len(self.shots) > 0:
            for i in range(len(self.shots)):
                draw.circle(self.screen, self.shots[i]["color"], (int(self.shots[i]["posi"][x]), int(self.shots[i]["posi"][y])), self.radius)
    