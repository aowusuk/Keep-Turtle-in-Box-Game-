
import turtle 

wn = turtle.Screen()
wn.title("Keep the Turtle Home")
wn.bgcolor("Dark Blue") 
wn.setup(width=800, height=600)
wn.tracer(0)  #stops window from updating, would be slow otherwise

#Score Keeping
score_a = 0
score_b = 0



#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  #set module to max speed
paddle_a.shape("square") # default 20p by 20p
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)     # 100 x 20 stretch default shape size
paddle_a.penup()  #line?
paddle_a.goto(-350, 0) #position it starts at x y 

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  #set module to max speed
paddle_b.shape("square") # default 20p by 20p
paddle_b.color("pink")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)     # 100 x 20 stretch default shape size
paddle_b.penup()  #line?
paddle_b.goto(350, 0)
                                     #all good at this point

#Ball
ball = turtle.Turtle()
ball.speed(0)  #set module to max speed
ball.shape("turtle") # default 20p by 20p
ball.color("green")
ball.penup()  #line?
ball.goto(0, 0)   #middle   -400 0 +400
ball.dx = 0.15    #move to the right 2
ball.dy = 0.15        #move to the left 2   connect to main loop

#pen
pen = turtle.Turtle()
pen.speed(0)   #animation speed
pen.color("white")
pen.penup()     #stop line from moving
pen.hideturtle() #hide turtle not text
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))




#Function
def paddle_a_up():
	y = paddle_a.ycor()     #get y cord, name of paddle puls turtle function that returns quardinate
	y += 20                     #add 20 to cordinate
	paddle_a.sety(y)             #set y of coordinate to new y coordinate

def paddle_a_down():
	y = paddle_a.ycor()     
	y -= 20                    
	paddle_a.sety(y) 

def paddle_b_up():
	y = paddle_b.ycor()     
	y += 20                     #add 20 to cordinate
	paddle_b.sety(y)             #set y of coordinate to new y coordinate

def paddle_b_down():
	y = paddle_b.ycor()     
	y -= 20                    
	paddle_b.sety(y)


#keyboard binding
wn.listen()             #listen for keyboard input
wn.onkey(paddle_a_up, "w")   #when the user presses w call "paddleaup" function onkeypress python 3 onkey python 2 
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")   #when the user presses w call "paddleaup" function onkeypress python 3 onkey python 2 
wn.onkey(paddle_b_down, "Down")


#main game loop
while True:
	wn.update()     #opens screen at this point

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#avoid border of screen being hit, contrict ball to stay in lines
	if ball.ycor() > 290:   #if cordinates is more than 290
		ball.sety(290)
		ball.dy *= -1    #reverses direction 
	elif ball.ycor() < -290:   #if cordinates is less than -290
		ball.sety(-290)
		ball.dy *= -1    

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1              #adds 1  VV changes whats in brakets
		pen.clear()       #clear text score
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



	elif ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



		#ball and paddle collision
	
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor > paddle_b.ycor() - 40): 
		ball.setx(340)
		ball.dx *= -1

	elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor > paddle_a.ycor() - 40): 
		ball.setx(-340)
		ball.dx *= -1
