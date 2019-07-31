import turtle

loadWindow = turtle.Screen()

turtle.speed(5)
turtle.pensize(2)


def fib(n):
    a = 0
    b = 10
    global y
    y = []

    for i in range(0, n):
        c = a + b
        a = b
        b = c
        y.append(c)
    return y


fib(9)
print(y)


# initial square
def turtle_square1(y):
    for n in y:
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n)


turtle_square1(y)

turtle.exitonclick()
