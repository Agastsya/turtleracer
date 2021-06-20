from turtle import Turtle, Screen
import random


screen = Screen()
screen.bgpic('203.gif')

coordinates_y = [-260, -180, -100, -20, 60]
colors = ["red", "blue", "green", "cyan", "yellow"]
user = screen.textinput(title="RACING", prompt="WHICH IS THE ONE YOU WANNA BET ON")
screen.setup(800, 800)
racers = []


for x in range(5):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colors[x])
    racer.goto(x=-300, y=coordinates_y[x])
    racer.clear()
    racers.append(racer)

if user:
    race_status = True

while race_status:
    for racer in racers:
        if racer.xcor() > 380:
            race_status = False
            winner = racer.pencolor()
            if winner == user:
                print(f"{winner} Racer is the winner, you made the right choice ")
            else:
                print(f"{winner} Racer is the winner, you lost this one try next time")
        distance = random.randint(0, 10)
        racer.forward(distance)

screen.exitonclick()
