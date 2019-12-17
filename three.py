import turtle


def circlefill(t,x,y,r):
	print("three circle")
	t.penup()
	t.goto(x,y+r)
	t.down()
	t.begin_fill()
	t.color("#0000ff")
	for i in range (1,40):
		t.forward(10)
		t.rt(9)
	t.end_fill()
	
def arc(t,x,y,l,tn,h):
	#x, y l(length) tn(turn value)
	t.down()
	t.setheading(0)
	t.heading()
	t.seth(h)
	for i in range (1,20):
		t.forward(l)
		t.rt(tn)
	
def three3(t):
	x = 0; y = 0
	arc(t,x,y,40,13,270)
	circlefill(t,x,y,50)


def main():
	w = turtle.Screen()
	w.setup(700, 700)
	w.clear()
	w.bgcolor("#ff7f00")
	t = turtle.Turtle()
	w.exitonclick()

if __name__ == '__main__':
	main()
	
'''
#apt install python3-tk
	


wn = turtle.Screen()   # create a turtle
t = turtle.Turtle()
t.color('green')      # set the color
t.forward(50)         # draw a green line of leng
t.up()                # lift up the tail
t.forward(50)         # move forward 50 without drawing
t.right(90)           # change direction to the right, left works too
t.down()              # put the tail down
t.backward(100)       # draw a green line 100 units long
wn.exitonclick()
'''
