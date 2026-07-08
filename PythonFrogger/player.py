from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y and self.heading() == 90:
            self.setheading(270)

    def is_at_finish_line(self):
        if self.ycor() < -FINISH_LINE_Y and self.heading() == 270:
            self.setheading(90)
            return True
        else:
            return False