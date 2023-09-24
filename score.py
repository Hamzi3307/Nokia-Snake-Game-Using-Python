from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 12, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("green")
        self.score = 0
        self.goto(0, 270)
        self.show_score()
        
    def show_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()
