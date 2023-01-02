# draw Rectangle in Python Turtle

# Importing the Turtle Graphics Library
import turtle

#Same as the PEN UP function in SNAP
turtle.penup()

#Setting the starting X,Y position of the cursor
turtle.setposition(-350,225)

#Same as the PEN DOWN function in SNAP
turtle.pendown()

#This one of the commands to fill in the rectangle
turtle.begin_fill()

# drawing first side
turtle.forward(50) # Forward turtle by l units
turtle.left(90) # Turn turtle by 90 degree
 
# drawing second side
turtle.forward(100) # Forward turtle by w units
turtle.left(90) # Turn turtle by 90 degree
 
# drawing third side
turtle.forward(50) # Forward turtle by l units
turtle.left(90) # Turn turtle by 90 degree
 
# drawing fourth side
turtle.forward(100) # Forward turtle by w units
turtle.left(90) # Turn turtle by 90 degree

#This other command to fill in the rectangle
turtle.end_fill()

#This keeps the graphics screen visible until it is clicked on
turtle.Screen().exitonclick() 