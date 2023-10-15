import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data = pd.read_csv("50_states.csv")
state_names = state_data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()

    if answer_state in state_names:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = state_data[state_data.state == answer_state]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(answer_state)


    if answer_state == "Exit":
        break

missed_states = [state for state in state_names if state not in guessed_states]
new_data = pd.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")
