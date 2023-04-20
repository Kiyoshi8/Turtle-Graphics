import turtle

t=turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(1)
t.color('green')
t.left(90)
t.backward(100)
t.speed(100)
t.shape('turtle')

def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color('red')
        t.circle(2)
        t.color('violet')
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(100)
turtle.done()
