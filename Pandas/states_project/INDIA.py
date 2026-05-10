import turtle
import pandas

'''
The only problem is the coordinates of india are some are correct and some are not accuarte cause i manually adjusted the coordinates
of each state so it takes lot time for those even few i adjusted so i leaved some of states same as the normal coordinate
'''



#to figure our coordinates(x,y)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen = turtle.Screen()
screen.title("INDIA States Game")
screen.setup(width=700, height=500)
image = "India-map-insize.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("india_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("india_states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
