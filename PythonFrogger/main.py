import time
from turtle import Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard

WIDTH, HEIGHT = 600, 600
difficulty = 10

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)
screen.listen()
screen.colormode(255)

player = Player()
car = Car_Manager(difficulty)
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # collision with car
    for crashed_car in car.all_cars:
        if crashed_car.distance(player) < 18:
            game_is_on = False
            scoreboard.game_over()

    # scoring, cars move faster after each point scored
    if player.is_at_finish_line():
        scoreboard.update_score()
        car.increase_speed()
        if difficulty == 5:
            pass
        else:
            difficulty -= 1

screen.exitonclick()