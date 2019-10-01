#Only top bar of keyboard and "a" are programmed
first=input("Pick a letter from the top bar of the keyboard: ")              #Starting inputs here
second=input("Pick another letter from the top bar of the keyboard: ")
third=input("Pick yet another letter from the top bar of the keyboard: ")
fourth=input("Pick a final letter from the top bar of the keyboard: ")
x = 0
y = 0
def hehe (x, y):                #Definitions
        t.goto(x,y)
        t.pendown
        t.write("hehe")

def star1 (x, y):
     t.pendown
     t.left(75)
     t.right(90)
     t.backward(75)
     t.right(75)
     t.forward(25)
     t.backward(65)
     t.right(45)
        
import turtle as t              #Turtle entered as "t" for simplicity
t.shape("turtle")

if first == "a" or second == "a" or third == "a" or fourth == "a":                      #All programs listed here
    counter = 0
    t.penup
    t.pencolor("blue")
    t.speed(10)
    for hh in range(10):
        hehe(x, y)
        x = x + 20

if first == "q" or second == "q" or third == "q" or fourth == "q":
    t.penup
    counter = 0
    t.pencolor("red")
    for hh in range(20):
        star1(x,y)
        y = y +5

if first == "w" or second == "w" or third == "w" or fourth == "w":
    counter = 0
    t.penup
    t.pencolor("blue")
    while counter < 5:
        t.goto(100,0)
        t.pendown
        t.left(70)
        t.right(54)
        t.backward(23)
        t.right(76)
        t.forward(35)
        t.backward(31)
        t.right(67)
        counter = counter+1
        
if first == "e" or second == "e" or third == "e" or fourth == "e":
    t.pencolor
    t.bgcolor("black")
            
if first == "r" or second == "r" or third == "r" or fourth == "r":
    counter = 0
    t.penup
    t.pencolor("purple")
    while counter < 6:
        t.goto(-100,50)
        t.pendown
        t.left(25)
        t.right(45)
        t.backward(65)
        t.right(90)
        t.forward(75)
        t.right(45)
        t.left(90)
        t.backward(90)
        counter = counter+1

if first == "t" or second == "t" or third == "t" or fourth == "t":
    counter = 0
    t.penup
    t.pencolor("yellow")
    while counter < 5:
        t.goto(-150,--150)
        t.pendown
        t.left(75)
        t.right(35)
        t.backward(65)
        t.right(25)
        t.right(50)
        t.forward(100)
        counter = counter+1

if first == "y" or second == "y" or third == "y" or fourth == "y":
    counter = 0
    t.penup
    t.pencolor("cyan")
    while counter < 5:
        t.goto(150,150)
        t.pendown
        t.left(100)
        t.right(35)
        t.backward(75)
        t.right(100)
        t.forward(65)
        t.left(90)
        t.backward(75)
        counter = counter+1

if first == "u" or second == "u" or third == "u" or fourth == "u":
    counter = 0
    t.penup
    t.pencolor("white")
    while counter < 5:
        t.goto(0,150)
        t.pendown
        t.right(50)
        t.right(50)
        t.right(50)
        t.right(50)
        counter = counter+1

if first == "i" or second == "i" or third == "i" or fourth == "i":
    counter = 0
    t.penup
    t.pencolor("pink")
    t.speed(500)
    while counter < 50:
        t.goto(150,150)
        t.pendown
        t.right(100)
        t.forward(100)
        t.left(100)
        t.backward(100)
        t.left(65)
        t.backward(45)
        t.right(75)
        counter = counter+1

if first == "o" or second == "o" or third == "o" or fourth == "o":
    counter = 0
    t.penup
    t.pencolor("orange")
    t.speed(500)
    while counter < 50:
        t.goto(0,-150)
        t.pendown
        t.right(100)
        t.forward(50)
        t.left(100)
        t.backward(100)
        t.left(65)
        t.backward(125)
        t.right(75)
        counter = counter+1

if first == "p" or second == "p" or third == "p" or fourth == "p":
    counter = 0
    t.penup
    t.pencolor("brown")
    t.speed(500)
    while counter < 50:
        t.goto(150,-150)
        t.pendown
        t.right(75)
        t.forward(60)
        t.left(125)
        t.backward(65)
        t.left(90)
        t.backward(75)
        t.right(75)
        counter = counter+1


