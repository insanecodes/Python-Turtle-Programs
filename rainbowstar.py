import turtle

length=100
size=400

colors=['red','orange','yellow','green','blue','Indigo','violet']

turtle.speed(7)
turtle.pensize(10)

for i in colors:
    size=500
    turtle.penup()
    turtle.goto(-size/2,size/10)
    turtle.pendown()
    turtle.color(i)
    turtle.begin_fill()

    for j in range(5):
        turtle.fd(size)
        turtle.rt(144)
    turtle.end_fill()

turtle.mainloop()
