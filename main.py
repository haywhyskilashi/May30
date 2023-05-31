
import turtle
import math
wn = turtle.Screen()

june = turtle.Turtle()
# may = turtle.Turtle()
w2 = turtle.Turtle()
w1 = turtle.Turtle()
downdoor = turtle.Turtle()
upwindow1 = turtle.Turtle()
upwindow2 = turtle.Turtle()
topdoor = turtle.Turtle()

#
# def move_right():
#     may.penup()
#     may.setheading(200)
#     may.fd(170)
#
# def draw_square():
#     may.fillcolor("red")
#     may.pendown()
#     may.begin_fill()
#     may.right(50)
#     may.forward(20)
#
#
#
#
# wn.onkey(move_right(), 'right')
# wn.onkey(draw_square(), 's')
#
#
#


june.hideturtle()
for i in range(2):
    june.color("blue")
    june.right(90)
    june.forward(100)
    june.right(90)
    june.forward(170)
june.left(90)
june.forward(100)
june.left(90)
june.forward(170)



dist = math.sqrt(170 * 170 / 2)

june.right(135)
june.forward(dist)
june.right(90)
june.forward(dist)
june.right(135)
june.forward(170)
june.left(90)
june.forward(100)

x = (90, 180)
y = (100, 240)
#
# may.penup()
# may.goto(x)
# #may.pendown()
# may.goto(y)
#
# may.color("green")

w2.up()
w2.goto(-40, -50)
w2.pendown()
w2.hideturtle()


for i in range(4):
    w2.forward(25)
    w2.left(90)

w1.up()
w1.goto(-120, -50)
w1.pendown()
w1.hideturtle()


for i in range(4):
    w1.left(90)
    w1.forward(25)

downdoor.up()
downdoor.goto(-100, -25)
downdoor.pendown()
downdoor.hideturtle()



downdoor.forward(40)
downdoor.right(90)
downdoor.forward(70)
downdoor.right(90)
downdoor.forward(40)
downdoor.right(90)
downdoor.forward(70)

upwindow1.up()
upwindow1.goto(-10, 50)
upwindow1.pendown()
upwindow1.hideturtle()

for i in range(4):
    upwindow1.left(90)
    upwindow1.forward(25)


upwindow2.up()
upwindow2.goto(-120, 50)
upwindow2.pendown()
upwindow2.hideturtle()

for i in range(4):
    upwindow2.left(90)
    upwindow2.forward(25)


topdoor.up()
topdoor.goto(-100, 5)
topdoor.pendown()
topdoor.hideturtle()



topdoor.forward(40)
topdoor.left(90)
topdoor.forward(70)
topdoor.left(90)
topdoor.forward(40)
topdoor.left(90)
topdoor.forward(70)
topdoor.pendown()



# def makeshape(numsides):
#     for i in range(numsides):
#         may.forward(100)
#         may.left(360.0 / numsides)
#
# makeshape(3)
#
# for i in range(2, 11):
#     makeshape(i)
wn.exitonclick()
