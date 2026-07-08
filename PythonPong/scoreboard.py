from turtle import Turtle

ALIGNMENT ="center"
FONT = ("Arial", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self, position, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.show_score()

    def show_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()
