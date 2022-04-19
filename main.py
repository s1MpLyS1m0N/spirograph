import turtle as t
from turtle import Screen
import random
from random import randint

t.speed("fastest")

screen = Screen()
screen.colormode(0)
screen.bgcolor("#0d1117")

# Generate random custom colours --start
color_list = []
n = 10
for i in range(n):
    color_list.append('#%06X' % randint(0, 0xFFFFFF))
# Generate random custom colours --end

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        t.color(random.choice(color_list))
        t.circle(180)
        t.setheading(t.heading() + 10)

draw_spirograph(5)

screen.exitonclick()