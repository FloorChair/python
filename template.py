import turtle

def main():
	w = turtle.Screen()
	w.setup(600, 600)
	w.clear()
	w.bgcolor("#ff7f00")
	t = turtle.Turtle()
	t.speed(0)
	
	draw_right_eye(t)
	draw_left_eye(t)
	draw_right_mouth(t)
	draw_left_mouth(t)
	draw_tooth_left(t)
	draw_tooth_right(t)
	sponge_bob_nose(t)
	eye_browleft_1(t)
	eye_browleft_2(t)
	eye_browleft_3(t)
	eye_browright_1(t)
	eye_browright_2(t)
	eye_browright_3(t)
	
	w.exitonclick()

def draw_left_eye(t):
  t.penup()
  t.begin_fill()
  t.fillcolor('#ffffff')
  t.setpos(-25,100)
  t.pendown()
  t.circle(15)
  t.end_fill()

def draw_right_eye(t):
  t.penup()
  t.begin_fill()
  t.fillcolor('#ffffff')
  t.setpos(25,100)
  t.pendown()
  t.circle(15)
  t.end_fill()

def draw_right_mouth(t):
  t.penup()
  t.setpos(0,50)
  t.width(3)
  t.pendown()
  t.circle(100,25)
  t.setheading(0)
 
def draw_left_mouth(t):
  t.penup()
  t.setpos(0,50)
  t.pendown()
  t.circle(100,-25)
  t.setheading(0)

def draw_tooth_left(t):
  t.width(1)
  t.penup()
  t.setpos(-20,52)
  t.pendown()
  t.begin_fill()
  t.fillcolor('#ffffff')
  t.right(90)
  t.forward(20) 
  t.left(90)
  t.forward(15)
  t.left(90)
  t.forward(18)
  t.end_fill()
  
def draw_tooth_right(t):
  t.penup()
  t.setpos(10,50)
  t.pendown()
  t.begin_fill()
  t.fillcolor('#ffffff')
  t.right(180)
  t.forward(18) 
  t.left(90)
  t.forward(15)
  t.left(90)
  t.forward(20)
  t.end_fill()
  
def sponge_bob_nose(t):
	t.penup()
	t.setpos(10,75)
	t.pendown()
	t.begin_fill()
	t.fillcolor('#e4f11c')
	t.right(90)
	for x in range(25):
		t.forward(3)
		t.right(1)
	t.right(45)
	t.forward(5)
	t.right(45)
	t.forward(5)
	t.right(90)
	for x in range(25):
		t.forward(3)
		t.left(1)
	t.end_fill()

def eye_browleft_1(t):
	t.penup()	
	t.setpos(-25,130)
	t.pendown()
	t.right(90)
	t.forward(15)
	
	
def eye_browleft_2(t):
	t.penup()	
	t.setpos(-35,125)
	t.pendown()
	t.left(15)
	t.forward(15)
	
def eye_browleft_3(t):
	t.penup()	
	t.setpos(-15,125)
	t.pendown()
	t.right(30)
	t.forward(15)
	
def eye_browright_1(t):
	t.penup()	
	t.setpos(25,130)
	t.pendown()
	t.left(15)
	t.forward(15)	
	
def eye_browright_2(t):
	t.penup()	
	t.setpos(35,125)
	t.pendown()
	t.right(20)
	t.forward(15)
	
def eye_browright_3(t):
	t.penup()	
	t.setpos(15,125)
	t.pendown()
	t.left(36)
	t.forward(15)
	t.hideturtle()
	
	
if __name__ == '__main__':
	main()
	
