import turtle
colors = ['red', 'orange','yellow','green','blue','purple']
mitch = turtle.Turtle()
turtle.bgcolor('black')
mitch.speed('normal') #new
# outer loop of for six squares
for n in range (6):
    mitch.color(colors[n])
    #inner loop to draw squares
    for i in range(4):
        mitch.forward(20)
        mitch.right (90)
    mitch.penup()
    mitch.forward(30)
    mitch.pendown()
mitch.hideturtle()
turtle.exitonclick()