"""
Pacotes necessarios para instalar:

pip install PythonTurtle

"""

import turtle

try:
    turtle.title("Trevo de 4 Folhas")

    cores_contorno = ['#29e38f', '#29e38f', '#29e38f', '#29e38f']

    angulo_inclinacao = 50

    def configure_turtle():
        screen = turtle.Screen()
        screen.bgcolor('black')
        
        pen = turtle.Turtle()
        pen.shape('circle')  
        pen.shapesize(0.1, 0.1)
        pen.speed(0)  
        return pen

    def curve(pen):
        for i in range(200):
            pen.right(1)
            pen.forward(1)

    def draw_heart(pen, cor_contorno):
        pen.color('#ffffff')
        pen.fillcolor(cor_contorno)
        pen.begin_fill()
        pen.left(140)
        pen.forward(113)
        curve(pen)
        pen.left(120)
        curve(pen)
        pen.forward(112)
        pen.end_fill()

    def draw_clover():
        pen = configure_turtle()

        for i in range(len(cores_contorno)):
            draw_heart(pen, cores_contorno[i])
            pen.left(angulo_inclinacao)

        pen.hideturtle()


    pen = configure_turtle()
    pen.penup()
    pen.goto(0, 250)  
    pen.color("#29e38f")  
    pen.write("Trevo de 4 Folhas", align='center', font=("Arial", 20, "bold"))
    pen.hideturtle()

    draw_clover()  
    turtle.done()
except:
    pass      