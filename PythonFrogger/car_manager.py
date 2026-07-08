from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5
START_X = 310
STARTING_SPEED = 5
CAR_SHAPES = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

class Car_Manager():
    def __init__(self, difficulty) -> None:
        self.all_cars = []
        self.difficulty = difficulty
        self.car_speed = STARTING_SPEED

    def create_car(self):
        rng_car_gen = random.randint(1,self.difficulty)
        if rng_car_gen == 1:
            car = Turtle()
            car.penup()
            car.shape(random.choice(CAR_SHAPES))
            #car.shape("square")
            #car.shapesize(stretch_wid=1, stretch_len=2)
            #car.colo(random.choice(COLORS))
            car.color(self.random_color())
            car.setposition(START_X, random.randint(-240, 240))
            car.setheading(180)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)

    def increase_speed(self):
        self.car_speed += 1

    def random_color(self):
        red = random.randint(0, 200)
        green = random.randint(0, 200)
        blue = random.randint(0, 200)
        colors = (red, green, blue)
        return colors