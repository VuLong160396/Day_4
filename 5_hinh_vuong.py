import turtle
t = turtle.Turtle()
t.speed(3)
def hinh_vuong():
    for i in  range(4):
        t.forward(100)
        t.right(90)
def dinh_cao_hinh_vuong():
    t.right(-15)
    for i in range(5):
        hinh_vuong()
        t.forward(50)
        t.right(72)
        t.backward(50)
dinh_cao_hinh_vuong()

turtle.done()
