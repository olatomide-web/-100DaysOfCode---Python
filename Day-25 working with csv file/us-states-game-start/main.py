import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "image.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}" , prompt="what's another states name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            missing_states.append(state)
            print(missing_states)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(answer_state)




screen.exitonclick()