import turtle
t = turtle.Turtle()
def ve_nha():
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
def mai_nha():
    t.fillcolor("purple")
    t.begin_fill()
    t.right(-45)
    t.forward(70)
    t.right(90)
    t.forward(70)
    t.end_fill()
    t.fillcolor("orange")
    t.begin_fill()
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.end_fill()
    t.fillcolor("yellow")
    t.begin_fill()
    t.left(90)
    t.forward(70)
    t.right(45)
    t.forward(100)
    t.left(135)
    t.forward(70)
    t.left(45)
    t.forward(100)
    t.left(135)
    t.forward(70)
    t.end_fill()
def cua_so():
    t.fillcolor("red")
    t.begin_fill()
    t.penup()
    t.goto(130,-10)
    t.pendown()
    t.forward(20)
    t.left(45)
    t.forward(30)
    t.left(135)
    t.forward(20)
    t.left(45)
    t.forward(30)
    t.end_fill()
def cua_chinh():
    t.fillcolor("green")
    t.begin_fill()
    t.penup()
    t.goto(70,-50)
    t.pendown()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.end_fill()
def mat_troi():
    t.fillcolor("yellow")
    t.begin_fill()
    t.penup()
    t.goto(250,200)
    t.pendown()
    t.circle(50)
    t.end_fill()
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(100,200)
    t.pendown()
    t.forward(50)
    t.penup()
    t.goto(200,250)
    t.pendown()
    t.left(90)
    t.forward(50)
    t.penup()
    t.goto(200,100)
    t.pendown()
    t.forward(50)
    t.backward(50)
    t.penup()
    t.goto(150,150)
    t.pendown()
    t.right(45)
    t.forward(20)
    t.penup()
    t.forward(100)
    t.pendown()
    t.forward(20)
    t.penup()
    t.goto(150,250)
    t.right(90)
    t.pendown()
    t.forward(20)
    t.penup()
    t.goto(250,150)
    t.pendown()
    t.backward(20)
def ve_cay():
    t.penup()
    t.fillcolor("brown")
    t.begin_fill()
    t.goto(200,-100)
    t.pendown()
    t.left(45)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.end_fill()
    t.backward(40)
    t.left(90)
    t.forward(10)

    t.fillcolor("green")
    t.begin_fill()
    for i in range(3):
        t.forward(30)
        t.left(120)
        t.forward(30)
    t.end_fill()
    t.left(90)
    t.penup()
    t.forward(50)
    t.right(90)
    t.fillcolor("green")
    t.begin_fill()
    t.pendown()
    for i in range(3):
        t.forward(20)
        t.left(120)
        t.forward(20)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(35)
    t.right(90)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.pendown()
    for i in range(3):
        t.forward(10)
        t.left(120)
        t.forward(10)
    t.end_fill()
turtle.bgcolor("teal")
t.speed(10)
ve_nha()
mai_nha()
cua_so()
cua_chinh()
mat_troi()
ve_cay()
t.penup()
t.goto(50,-120)
t.shape("turtle")
t.color("red")
t.left(90)
t.pendown()
#turtle.bgcolor("green")
turtle.done()