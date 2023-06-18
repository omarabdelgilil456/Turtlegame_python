import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = -100
for x in range(6):
    tr = Turtle("turtle")
    tr.penup()
    tr.color(colors[x])
    tr.goto(-230, y)
    y += 50
    turtles.append(tr)
race_on = True
while race_on:
    for tr in turtles:
        if tr.xcor() > 230:
            winner_turtle = tr.pencolor()
            race_on = False
            if user_bet == winner_turtle:
                print(f"you've won! winning turtle is {winner_turtle}")
                break
            else:
                print(f"you've lost! winning turtle is {winner_turtle}")
                break
        tr.forward(random.randint(1, 10))

screen.exitonclick()
