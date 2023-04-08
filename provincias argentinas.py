import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. state Game")
imagen = "blank_states_img.gif"
screen.addshape(imagen)
turtle.shape(imagen)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
estados_adivinados = []

while len(estados_adivinados) < 50:
    respuesta_state = screen.textinput(title=f"{len(estados_adivinados)}/50 estados",
                                       prompt="nombra otro estado de USA").title()
    if respuesta_state == "Exit":
        estados_faltantes = [estado for estado in all_state if estado not in estados_adivinados]
       # for estados in all_state:
       #     if estados not in estados_adivinados:
        #        estados_faltantes.append(estados)
        new_data = pandas.DataFrame(estados_faltantes)
        new_data.to_csv("estados para aprender")
        break
    if respuesta_state in all_state:
        estados_adivinados.append(respuesta_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == respuesta_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(respuesta_state)


