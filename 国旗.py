import turtle                   # 调用小海龟库


def location(a, b):             # 定位五角星位置
    turtle.up()
    turtle.goto(a, b)
    turtle.down()


def pentagram(s):               # 画五角星
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(s)
        turtle.right(144)
    turtle.end_fill()


turtle.setup(600, 400, 0, 0)    # 生成画板
turtle.color("yellow")
turtle.bgcolor("red")
turtle.fillcolor("yellow")

location(-250, 95)
pentagram(100)

for i in range(4):
    x = 1
    if i in [0, 3]:
        x = 0
    location(-120 + x * 30, 150 - i * 40)
    turtle.left(15 - i * 15)
    pentagram(30)

turtle.hideturtle()             # 隐藏小海龟
turtle.done()                   # 维持画板
