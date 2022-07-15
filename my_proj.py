import turtle
a=turtle.Turtle()
for _ in range(4):
    if _%2==0:
        a.forward(100)
        a.right(90)
    else:
        a.forward(100)
        a.right(90)
# a.forward(10)
b=turtle.Screen()
b.bgcolor("blue")
a.penup()
from  turtle import *
speed(1)
width(4)
bgcolor('black')
color('blue')
begin_fill()
penup()
goto(-50,60)
pendown()
goto(100,100)
goto(100,-100)
goto(-50,-60)
goto(-50,60)
end_fill()
penup()
color('black')
width(10)
goto(-50,0)
pendown()
goto(100,0)
penup()
goto(25,80)
pendown()
goto(25,-80)
done()

# from  turtle import *
# left(90)
# for i in range(20):
#     forward(100+10*i)
#     left(90)

# right(90)
# forward(100)
# for i in range(20):
#     forward(100+10*i)
#     right(90)

# print(position())
# setx(20)
# print(position())
left(90)
# for i in range(4):
#     forward(100)
#     right(90)
#     forward(20)
#     right(90)
#     forward(100)
   
  # set the x coordinate
    # up()
    # setx(40*(i+1))
    # down()
   
  # change the direction
    # left(180)

# right(90)
# for i in range(4):
#     forward(100)
#     right(90)
#     forward(20)
#     right(90)
#     forward(100)
#     up()
#     sety(-40*(i+1))
#     down()
#     left(180)
   
# forward(100)
# dot(60,'blue')
# dot(90, "yellow")