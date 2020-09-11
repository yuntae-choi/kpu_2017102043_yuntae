import turtle
k=0
for i in range(0,5):
	for i in range(0,5):
		turtle.forward(100)
		turtle.left(90)
		turtle.forward(100)
		turtle.left(90)
		turtle.forward(100)
		turtle.left(90)
		turtle.forward(100)
		turtle.left(90)
		turtle.forward(100)
	turtle.penup()
	k=k-100
	turtle.goto(0,k)
	turtle.pendown()
