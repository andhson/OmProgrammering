import turtle

#https://realpython.com/beginners-guide-python-turtle/

# Get screen and Turtel.
s = turtle.getscreen()
t = turtle.Turtle()

# Change Turtel bar.
turtle.title("Västerskolans sköldpadda ritar")

# Change Turtel size,color and looks.
#t.shape("arrow")
t.shape("turtle")
#t.shapesize(2,1,1)
t.fillcolor("orange")

t.right(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.penup()

'''
# Draw square and lift pen.
t.right(90)
t.forward(200)
for ix in range(1,4):
    t.left(90)
    t.forward(200)
    #print(ix)
t.penup()
'''

'''
# Draw square and lift pen.
l = 200
a = 90
t.right(a)
t.forward(l)
for ix in range(1,4):
    t.left(a)
    t.forward(l)
    #print(ix)
t.penup()    
'''

# Change background.
turtle.bgcolor("green")

# Draw circel and go home, argument is radius. Change pensize.
t.pensize(2)
t.speed(1)
t.goto(100,0)
t.pendown()
t.circle(100)
t.penup()
t.home()

# Ask to draw a triangel and go home.
#u = input('Vill du rita en triangel (j/n)? ')
u = 'j'

if u == 'j':
    t.goto(100,0)
    t.pensize(4)
    t.speed(5)
    t.pendown()
    t.goto(200,-100)
    t.goto(0,-100)
    t.goto(100,0)
    t.penup()
    t.home()
else:
    print('Tack, då vet jag.')
    print('Hej då!')
    print(':-)')

turtle.bgcolor("orange")

# Change Turtel size back to default.
t.shapesize(1,1,1)

t.penup()
t.home()
#t.goto(0,0)
t.fillcolor("green")
t.begin_fill()
#t.clear()
#t.reset()