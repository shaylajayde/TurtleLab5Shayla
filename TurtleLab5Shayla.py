#Turtle Lab 5
#Bob Ross
#Shayla Zilinsky

import turtle
import time

def BobRoss():
    landscape = str()
    horizontal = int()
    vertical = int()
    answer = ""
    turtle.setup(800,600)
    turtle.shape("turtle")
    turtle.write("Let's get crazy.", align="center", font=("Arial", 15, "bold"))
    time.sleep(3)
    turtle.clearscreen()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    #user inputs what they would like to paint
    while answer != "Q":
        landscape = str(input("What would you like to paint today? A mountain? A happy little tree? A cabin? It's all in your hands. "))
        if landscape == "mountain":
            turtle.pencolor("black")
            turtle.fillcolor("green")
            turtle.pensize(10)
            horizontal = 0
            vertical = 0
            for count in range (0,3):
            #drawing the mountains
                turtle.goto(horizontal, vertical)
                turtle.pendown()
                turtle.begin_fill()
                turtle.forward(100)
                turtle.left(120)
                turtle.forward(100)
                turtle.left(120)
                turtle.forward(100)
                turtle.left(120)
                turtle.end_fill()
                horizontal = horizontal - 50
                turtle.penup()
        elif landscape == "happy little tree":
            turtle.pencolor("green")
            turtle.fillcolor("green")
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
            turtle.pencolor("brown")
            turtle.fillcolor("brown")
            turtle.penup()
            turtle.goto(-20,-20)
            turtle.pendown()
            #drawing the tree
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
            time.sleep(3)
            turtle.clearscreen()
            turtle.write("There's nothing wrong with having a tree as a friend. - Bob Ross", align ="center", font=("Arial", 15, "bold"))
        elif landscape == "cabin":
            turtle.pencolor("black")
            turtle.fillcolor("brown")
            #drawing the base of cabin
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
            turtle.fillcolor("black")
            turtle.penup()
            turtle.goto(50,150)
            turtle.pendown()
            #drawing the roof of cabin
            turtle.begin_fill()
            turtle.right(35)
            turtle.forward(125)
            turtle.right(235)
            turtle.forward(150)
            turtle.left(127)
            turtle.forward(130)
            turtle.end_fill()
        else:
            turtle.write("Darn, we haven't learned that skill yet.", align ="center", font=("Arial", 15, "bold"))
        time.sleep(5)
        turtle.reset()
        answer = str(input("Enter Q to quit: "))
    turtle.write("We don't make mistakes, just happy little accidents. - Bob Ross", align ="center", font=("Arial", 15, "bold"))
        


def main():
    BobRoss()
main()
        
        
        
        
        
        
