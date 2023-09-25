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
        with open("highscore.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as new:
                new.write(f"{self.high_score}")
            self.score = 0
            self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
