from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import random
import time

WIDTH, HEIGHT = 800, 600

HIT_P1_PADDLE = [45, 60, 75, 285, 300, 315]
HIT_P2_PADDLE = [135, 150, 165, 195, 210, 225]

P1_START, P2_START = (-370, 0), (370, 0)
P1_SCORE_POS, P2_SCORE_POS = (-300, 225), (300, 225)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    colors = (red, green, blue)
    return colors


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Python Pong")
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)
screen.listen(xdummy=None, ydummy=None)
screen.update()

ball = Ball()
player_1 = Paddle(P1_START)
player_2 = Paddle(P2_START)
p1_scoreboard = Scoreboard(P1_SCORE_POS)
p2_scoreboard = Scoreboard(P2_SCORE_POS)

sleep = 0.05
is_playing = True

screen.onkeypress(key="w", fun=player_1.paddle_up)
screen.onkeypress(key="s", fun=player_1.paddle_down)
screen.onkeypress(key="o", fun=player_2.paddle_up)
screen.onkeypress(key="l", fun=player_2.paddle_down)

ball.move()

while is_playing:
    screen.update()
    time.sleep(sleep)
    ball.move()
    #player_1.color(player_1.random_color()) #uncomment this line for multicolored paddle
    #player_2.color(player_2.random_color()) #uncomment this line for multicolored paddle
    #screen.bgcolor(random_color())  # uncomment this line for multicolored background

    # prevents paddles from moving off screen
    if player_1.ycor() > 240:
        player_1.paddle_down()
    elif player_1.ycor() < -240:
        player_1.paddle_up()

    if player_2.ycor() > 240:
        player_2.paddle_down()
    elif player_2.ycor() < -240:
        player_2.paddle_up()

    # wall collision
    if ball.ycor() > (HEIGHT/2)-10:
        ball.bounce_y()
        ball.move()
    elif ball.ycor() < -(HEIGHT/2)+20:
        ball.bounce_y()
        ball.move()

    # wall collision scoring
    if ball.xcor() > (WIDTH/2):
        p1_scoreboard.update_score()
        time.sleep(0.5)     # slight pause when a player scores
        ball.refresh()
        time.sleep(sleep)
    elif ball.xcor() < -(WIDTH/2):
        p2_scoreboard.update_score()
        time.sleep(0.5)
        ball.refresh()
        time.sleep(sleep)

    # paddle collision
    def paddle_collision(ball, player):
        return abs(ball.xcor() - player.xcor()) < 20 and abs(ball.ycor() - player.ycor()) < 60

    # speed up ball when it hits a paddle
    if paddle_collision(ball, player_1):
        ball.bounce_x()
        ball.move_speed *= 0.01

    if paddle_collision(ball, player_2):
        ball.bounce_x()
        ball.move_speed *= 0.01

screen.exitonclick()


