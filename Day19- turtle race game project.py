from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ").lower
colors = ["red", "orange", "yellow" "green", "blue", "purple" ]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []






for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"you win! the {winning_color} turtle is the winner!")
            else:
                print(f"you lose, the {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

# def move_forward():
#     my_ijapa.forward(10)


# def move_backward():
#     my_ijapa.backward(10)

# def turn_left():
#     new_heading = my_ijapa.heading() + 10
#     my_ijapa.setheading(new_heading)

# def turn_right():
#     new_heading = my_ijapa.heading() - 10
#     my_ijapa.setheading(new_heading)


# def clear():
#     my_ijapa.clear()
#     my_ijapa.penup()
#     my_ijapa.home()
#     my_ijapa.pendown()

# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")

screen.exitonclick()