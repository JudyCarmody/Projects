from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"
POSITION = (250, 250)

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(POSITION)
        self.show_score()

    def show_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)