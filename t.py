import turtle
screen=turtle.Screen()
screen.bgcolor("light green")
y=turtle.Turtle()

def drawfourrays(t,length,radius):
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length+radius)
        t.left(90)

y.penup()
y.goto(85,110)
y.fillcolor("yellow")
y.pendown()
y.begin_fill()
y.circle(45)
y=end_fill()

y.penup()
y.goto(85,169)
y.pendown()
drawfourrays(y,85,54)
y.right(45)
drawfourrays(y,85,54)
y.left(45)
turtle.done()


# import turtle
# #color("red","yellow")
# bgcolor("black")
# speed(0)

# for i in range(200):
#     begin_fill()
#     forward(300-i)
#     left(170)
#     forward(300-i)
#     end.fill()
# # done()    import turtle
# Screen=turtle.Screen
# screen.bgcolor("lightpink")
# y=turtle.Turtle()

# def drawfourrays(t,length,radius):
#     for i in range(4):
#         t.penup()
#         t.forward(radius)
#         t.pendown()
#         t.forward(length)
#         t.penup()
#         t.backward(length+radius)
#         t.left(90)

# y.penup()
# y.goto(85,110)
# y.fillcolor("yellow")
# y.pendown()
# y.begin_fill()
# y.circle(45)
# y=end_fill()

# y.penup()
# y.goto(85,169)
# y.pendown()
# drawfourrays(y,85,54)
# y.right(45)
# drawfourrays(y,85,54)
# y.left(45)

# turtle.done()


# import turtle
# #color("red","yellow")
# bgcolor("black")
# speed(0)

# for i in range(200):
#     begin_fill()
#     forward(300-i)
#     left(170)
#     forward(300-i)
#     end.fill()
# done()    