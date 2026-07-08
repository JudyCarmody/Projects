from turtle import Turtle
import random

DIRECTION = [-10, 10]

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.shapesize(0.8)
        self.penup()
        self.x_move = random.choice(DIRECTION)
        self.y_move = random.choice(DIRECTION)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        #self.color(self.random_color())        # uncomment this line for multicolored ball

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors = (red, green, blue)
        return colors