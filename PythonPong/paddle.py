from turtle import Turtle
import random

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)
        self.showturtle()

    def paddle_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        #self.color(self.random_color())        # uncomment this line for multicolored paddle

    def paddle_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        #self.color(self.random_color())        # uncomment this line for multicolored paddle

    def random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors = (red, green, blue)
        return colors