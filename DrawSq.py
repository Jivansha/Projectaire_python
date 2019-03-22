import turtle


def draw_sq():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(10)
    brad.color("yellow")

    l=36
    while(l>0):
        j=4
        while(j>0):
            brad.forward(100)
            brad.right(90)
            j=j-1
        brad.right(10)
        l=l-1

    
    tri = turtle.Turtle()
    tri.shape("circle")
    tri.color("red")
    tri.speed(10)
    l=18
    while(l>0):
        j=3
        while(j>0):
            tri.backward(100)
            tri.right(120)
            j=j-1
        tri.right(20)
        l=l-1
    tri.right(90)    
    tri.forward(250)
    
##    ang = turtle.Turtle()
##    ang.shape("classic")
##    ang.color("blue")
##    k=5
##    t=180
##    while(k>0):
##        ang.circle(t)
##        ang.circle(-t)
##        t=t/2
##        k=k-1
##        
##
##    tri = turtle.Turtle()
##    tri.shape("circle")
##    tri.color("black")
##    i=3
##    while(i>0):
##        tri.backward(100)
##        tri.right(120)
##        i=i-1
    

    window.exitonclick()

draw_sq()
    
    
