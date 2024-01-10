# Star ===============
# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# t.speed(10)
# s.bgcolor("black")
# col = ("yellow", "red", "white","cyan")
# c = 0
# for i in range(50):
#     t.forward(i*10)
#     t.right(144)
#     t.color(col[c])
#     if c == 3:
#         c = 0
#     else:
#         c+=1

# -----------------------------------------------------------------------------------------

# Square ==============
# import turtle
# skk = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# col = ("yellow", "red", "white","cyan")
# c = 0
# for i in range(50):
#     skk.forward(i*10)
#     skk.forward(50)
#     skk.right(90)
     
#     skk.color(col[c])
#     if c == 3:
#         c = 0
#     else:
#         c+=1
# turtle.done()

# -----------------------------------------------------------------------------------------

# Python program to draw Rainbow Benzene using Turtle Programming ================
# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
# 	t.pencolor(colors[x%6])
# 	t.width(x//100 + 1)
# 	t.forward(x)
# 	t.left(59)

# -----------------------------------------------------------------------------------------

# Star =============
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# -----------------------------------------------------------------------------------------

# import turtle  
# # Creating turtle  
# t = turtle.Turtle()  
# s = turtle.Screen()  
# s.bgcolor("black")  
# t.pencolor("red")  
  
# a = 0  
# b = 0  
# t.speed(0)  
# t.penup()  
# t.goto(0,200)  
# t.pendown()  
# while(True):  
#     t.forward(a)  
#     t.right(b)  
#     a+=3  
#     b+=1  
#     if b == 210:  
#         break  
#     t.hideturtle()  
  
# turtle.done()  

# -----------------------------------------------------------------------------------------

# import turtle  
# # Creating turtle  
# t = turtle.Turtle()  
# s = turtle.Screen()  
# s.bgcolor("black")  
  
# turtle.pensize(2)  
  
# # To design curve  
# def curve():  
#     for i in range(200):  
#         t.right(1)  
#         t.forward(1)  
  
# t. speed(3)  
# t.color("red", "red")  
  
# t.begin_fill()  
# t.left(140)  
# t.forward(111.65)  
# curve()  
  
# t.left(120)  
# curve()  
# t.forward(111.65)  
# t.end_fill()  
# t.hideturtle()  
  
# turtle.mainloop() 

# -----------------------------------------------------------------------------------------

# Pizza -------------------
# import turtle
# background="black"
# crust="#ECA84F"
# sauce="#AD0509"
# cheese="#FBC70F"
# pepperoni=[[-70,105],[-85,175],[-25,50],[-15,100],[-25,150],[-30,205],[15,50],[20,120],[20,200],[60,156],[71,215],[80,90]]
# screen=turtle.Screen()
# screen.bgcolor(background)
# screen.title("my pizza")
# my_turtle=turtle.Turtle()
# my_turtle.pensize(5)
# my_turtle.shape("circle")
# def draw_circle(radius,line_color,fill_color):
#     my_turtle.color(line_color)#draw the circle with the defined line color
#     my_turtle.fillcolor(fill_color)#fill the circle
#     my_turtle.begin_fill()
#     my_turtle.circle(radius)
#     my_turtle.end_fill()
# def move_turtle(x,y):
#     my_turtle.up   #my_turtle.penup()
#     my_turtle.goto(x,y) #move the turtle
#     my_turtle.down   #my_turtle.pendown()
# draw_circle(150,crust,crust)  #first circle for the crust which is drawn and filled by the same color
# move_turtle(0,25)
# draw_circle(125, sauce, cheese) #second circle with our sauce color and filled with cheese color
# #draw pepperoni
# for i in pepperoni:
#     my_turtle.penup()
#     move_turtle(i[0],i[1])
#     draw_circle(10,sauce,sauce)
# move_turtle(0,150)
# my_turtle.color(background)

# for x in range(0,8):
#     my_turtle.pendown()
#     my_turtle.left(45)
#     my_turtle.forward(150)
#     my_turtle.penup()
#     my_turtle.backward(150)
# turtle.done()

# -----------------------------------------------------------------------------------------
# Clock -------------------

# from turtle import Turtle, Screen
# import datetime

# #creating window
# window = Screen()
# #setting window title
# window.title("Krazy:Digital Clock")
# #setting background color
# window.bgcolor("black")
# #setting height and width of window
# window.setup(width=1000, height=800)

# #creating outer circle
# circle = Turtle()
# circle.penup()
# circle.pencolor("#118893")
# circle.speed(0)
# circle.pensize(25)
# circle.hideturtle()
# circle.goto(0, -390)
# circle.pendown()
# circle.fillcolor("#17202A")
# circle.begin_fill()
# circle.circle(400)
# circle.end_fill()

# #creating hour hand
# hHand = Turtle()
# hHand.shape("arrow")
# hHand.color("white")
# hHand.speed(10)
# hHand.shapesize(stretch_wid=0.4, stretch_len=18)

# #creating minute hand
# mHand = Turtle()
# mHand.shape("arrow")
# mHand.color("white")
# mHand.speed(10)
# mHand.shapesize(stretch_wid=0.4, stretch_len=26)

# #creating second hand
# sHand = Turtle()
# sHand.shape("arrow")
# sHand.color("dark red")
# sHand.speed(10)
# sHand.shapesize(stretch_wid=0.4, stretch_len=36)

# #creating center circle
# centerCircle = Turtle()
# centerCircle.shape("circle")
# #setting color to white
# centerCircle.color("white")
# centerCircle.shapesize(stretch_wid=1.5, stretch_len=1.5)

# # numbers with pen
# pen = Turtle()
# pen.speed(0)
# pen.color("white")

# #number 1
# pen.penup()
# pen.hideturtle()
# pen.goto(170, 260)
# pen.write("1", align="center", font=("Algerian", 50, "bold"))

# #number 2
# pen.penup()
# pen.hideturtle()
# pen.goto(300, 140)
# pen.write("2", align="center", font=("Algerian", 50, "bold"))

# #number 3
# pen.penup()
# pen.hideturtle()
# pen.goto(340, -30)
# pen.write("3", align="center", font=("Algerian", 50, "bold"))

# #number 4
# pen.penup()
# pen.hideturtle()
# pen.goto(300, -200)
# pen.write("4", align="center", font=("Algerian", 50, "bold"))

# #number 5
# pen.penup()
# pen.hideturtle()
# pen.goto(170, -325)
# pen.write("5", align="center", font=("Algerian", 50, "bold"))

# #number 6
# pen.penup()
# pen.hideturtle()
# pen.goto(0, -370)
# pen.write("6", align="center", font=("Algerian", 50, "bold"))

# #number 7
# pen.penup()
# pen.hideturtle()
# pen.goto(-170, -325)
# pen.write("7", align="center", font=("Algerian", 50, "bold"))

# #number 8
# pen.penup()
# pen.hideturtle()
# pen.goto(-300, -200)
# pen.write("8", align="center", font=("Algerian", 50, "bold"))

# #number 9
# pen.penup()
# pen.hideturtle()
# pen.goto(-340, -30)
# pen.write("9", align="center", font=("Algerian", 50, "bold"))

# #number 10
# pen.penup()
# pen.hideturtle()
# pen.goto(-280, 140)
# pen.write("10", align="center", font=("Algerian", 50, "bold"))

# #number 11
# pen.penup()
# pen.hideturtle()
# pen.goto(-160, 260)
# pen.write("11", align="center", font=("Algerian", 50, "bold"))

# #number 12
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 300)
# pen.write("12", align="center", font=("Algerian", 50, "bold"))

# #Defining function to movie hour hand
# def movehHand():
#    currentHourInternal = datetime.datetime.now().hour
#    degree = (currentHourInternal - 15) * -30
#    currentMinuteInternal = datetime.datetime.now().minute
#    degree = degree + -0.5 * currentMinuteInternal
#    hHand.setheading(degree)
#    window.ontimer(movehHand, 60000)


# #Defining function to minute hand
# def movemHand():
#     currentMinuteInternal = datetime.datetime.now().minute
#     degree = (currentMinuteInternal - 15) * -6
#     currentSecondInternal = datetime.datetime.now().second
#     degree = degree + (-currentSecondInternal * 0.1)
#     mHand.setheading(degree)
#     window.ontimer(movemHand, 1000)

# #Defining function to second hand
# def movesHand():
#     currentSecondInternal = datetime.datetime.now().second
#     degree = (currentSecondInternal - 15) * -6
#     sHand.setheading(degree)
#     window.ontimer(movesHand, 1000)

# window.ontimer(movehHand, 1)
# window.ontimer(movemHand, 1)
# window.ontimer(movesHand, 1)
# window.exitonclick()

#  -------------------------------------------------------------------------------------
# Clock ----------------

# import turtle
# import time

# wndw = turtle.Screen()
# wndw.bgcolor("black")
# wndw.setup(width=600, height=600)
# wndw.title("Analogue Clock")
# wndw.tracer(0)

# # Create the drawing pen
# pen = turtle.Turtle()
# pen.hideturtle()
# pen.speed(0)
# pen.pensize(3)


# def draw_clock(hr, mn, sec, pen):

#     # Draw clock face
#     pen.up()
#     pen.goto(0, 210)
#     pen.setheading(180)
#     pen.color("green")
#     pen.pendown()
#     pen.circle(210)

#     # Draw hour hashes
#     pen.up()
#     pen.goto(0, 0)
#     pen.setheading(90)

#     for _ in range(12):
#         pen.fd(190)
#         pen.pendown()
#         pen.fd(20)
#         pen.penup()
#         pen.goto(0, 0)
#         pen.rt(30)

#     # Draw the hands
#     # Each tuple in list hands describes the color, the length
#     # and the divisor for the angle
#     hands = [("white", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
#     time_set = (hr, mn, sec)

#     for hand in hands:
#         time_part = time_set[hands.index(hand)]
#         angle = (time_part/hand[2])*360
#         pen.penup()
#         pen.goto(0, 0)
#         pen.color(hand[0])
#         pen.setheading(90)
#         pen.rt(angle)
#         pen.pendown()
#         pen.fd(hand[1])


# while True:
#     hr = int(time.strftime("%I"))
#     mn = int(time.strftime("%M"))
#     sec = int(time.strftime("%S"))

#     draw_clock(hr, mn, sec, pen)
#     wndw.update()
#     time.sleep(1)
#     pen.clear()

# wndw.mainloop()

# ---------------------------------------------------------------------------
# Iron Man -------------

# import turtle
# # Top Part
# piece1=[[(-40, 120), (-70, 260), (-130, 230), 
# (-170, 200), (-170, 100), (-160, 40), (-170, 10), 
# (-150, -10), (-140, 10), (-40, -20), (0, -20)],[(0, -20), 
# (40, -20), (140, 10), (150, -10), (170, 10), (160, 40),
# (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), 
# (0, 120)]]
# # Middle Part
# piece2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40),
#  (-176, 0), (-186, -30), (-186, -40), (-120, -170), 
# (-110, -210), (-80, -230), (-64, -210), (0, -210)],
# [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]
# #Bottom Part
# piece3=[[(-60, -220), (-80, -240), (-110, -220), 
# (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],[(0, -250), (20, -250), (30, -260), (60, -260),
#  (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]]
# turtle.hideturtle()
# turtle.bgcolor('#ba161e') #Dark Red
# turtle.setup(500,600)
# turtle.title("I AM IRONMAN")
# piece1Goto=(0,120)
# piece2Goto=(0,-30)
# piece3Goto=(0,-220)
# turtle.speed(2)
# def draw_piece(piece,pieceGoto):
#     turtle.penup()
#     turtle.goto(pieceGoto)
#     turtle.pendown()
#     turtle.color('#fab104') #Light Yellow
#     turtle.begin_fill()
#     for i in range(len(piece[0])):
#         x,y=piece[0][i]
#         turtle.goto(x,y)

#     for i in range(len(piece[1])):
#         x,y=piece[1][i]
#         turtle.goto(x,y)
#     turtle.end_fill()
# draw_piece(piece1,piece1Goto)
# draw_piece(piece2,piece2Goto)
# draw_piece(piece3,piece3Goto)
# turtle.hideturtle()
# turtle.done()

# ----------------------------------------------------------------------------
# Virus ==============
from turtle import *
speed(10)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

a = '12' + '56'
print(a)

v="[1,2,3]"
g=eval("[1,2,3]")
print(g)
print(g[0])
print(v)
print(v[0])

a = abs(*23)
print(a)

def x(a=2,b=3):
    a=12
    b=13
    print(a,b)
x(10,20)

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            print('Not Prime')
            break
        else:
            print('Prime')
            break
prime(7)


