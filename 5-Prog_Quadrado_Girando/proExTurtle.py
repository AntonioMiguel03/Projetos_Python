# Certifique-se de que o pacote 'turtle' está instalado.
# Você pode instalar usando pip:
# pip install PythonTurtle

import turtle

try:
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Quadrado Girando")
    
    tartaruga = turtle.Turtle()        
    tartaruga.shape("circle")

    tartaruga.shapesize(0.1, 0.1)
    tartaruga.color("white")  
    tartaruga.speed(10)  

    
    cores_hex = ["#12cee3", "#FF1493", "#F5F5DC", "#FFA500", "#800080"]

    
    def desenhar_quadrado():
        for i in range(4):
            tartaruga.color(cores_hex[i % len(cores_hex)])  
            tartaruga.forward(100)
            tartaruga.left(90)
    
    while True:
        desenhar_quadrado()
        tartaruga.left(10)
    
    turtle.done()
except:
    pass    