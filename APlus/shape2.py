import turtle

turtle.penup()
turtle.setposition(-350,225)
turtle.pendown()
turtle.begin_fill()

for x in range(2):
    turtle.forward(50) 
    turtle.left(90) 
    turtle.forward(100) 
    turtle.left(90) 

turtle.end_fill()
turtle.Screen().exitonclick() 