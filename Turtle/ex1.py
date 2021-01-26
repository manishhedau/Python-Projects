import turtle

my_turtle = turtle.Turtle()

# n = int(input('Enter The size of Rectangle : '))

""" Rectangle code """
# for _ in range(4):
#     my_turtle.forward(n)
#     my_turtle.left(90)

""" Triangle with fill color """
# my_turtle.color('red','skyblue')
# my_turtle.begin_fill()
# my_turtle.forward(n)
# my_turtle.left(135)
# my_turtle.forward(n+43)
# my_turtle.left(135)
# my_turtle.forward(n+10)
# my_turtle.end_fill()


# my_turtle.forward(n)
# my_turtle.left(137)
# my_turtle.forward(n+52)
# my_turtle.left(135)
# my_turtle.forward(n)
# my_turtle.end_fill()
import math

my_turtle.speed(2000)
my_turtle.color('red','yellow')
# my_turtle.begin_fill()

# for i in range(200):
#     my_turtle.forward(math.sqrt(i)*20)
#     # my_turtle.left(150.688)
#     my_turtle.left(170)
#     # my_turtle.forward(200)


# my_turtle.end_fill()

for i in range(1000):
    my_turtle.forward(math.sqrt(i)*3)
    my_turtle.left(i%180)

turtle.done()