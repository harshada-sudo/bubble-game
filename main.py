import turtle #module 
import math,random #random module

#set up screen
wn = turtle.Screen()
wn.setup(700,700) #set screen size
wn.bgcolor('black')
wn.tracer(4)

#create score variable
score = 0

#draw border
pen = turtle.Turtle()
pen.penup()
pen.color('white')
pen.setposition(-300,-300)
pen.pendown()
pen.pensize(3)
for side in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()    

#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup() #hide the trail
player.speed(0)

#create goals
max_goals = 10
goals = []

for count in range(max_goals):
    goals.append(turtle.Turtle())  
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300))

#set speed variable
speed = 1

#define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    speed -= 1

def is_collision(self,other):
    #collision checking
    a = self.xcor() - other.xcor()
    b = self.ycor() - other.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 20:
        return True
    else:
        return False
        
#keyboard binding
turtle.listen()
turtle.onkeypress(turn_left,"Left")
turtle.onkeypress(turn_right,"Right")
turtle.onkeypress(increase_speed,"Up")
turtle.onkeypress(decrease_speed,'Down')

while True:
    wn.update()
    player.forward(speed)  #player keeps on moving forward

    #boundry checking
    if player.xcor() > 300 or player.xcor() < -300:  #checking x co-ordinates
        player.left(180) 

    if player.ycor() > 300 or player.ycor() < -300:  #checking y co-ordinates
        player.left(180)
 
    #move goal
    for count in range(max_goals):
        goals[count].forward(3)  

        #boundry checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:  #checking x co-ordinates
            goals[count].left(180) 

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:  #checking y co-ordinates
            goals[count].left(180) 
        
        #collision checking
        if is_collision(player,goals[count]):
            goals[count].setposition(random.randint(-290,290),random.randint(-290,290))
            goals[count].right(random.randint(0,360))
            score += 1
            #draw score on screen
            pen.undo()
            pen.penup()
            pen.hideturtle()
            pen.setposition(0,310)
            pen.write("Score : {}".format(score),align = 'center',font= ('times new roman',15,'normal'))
wn.mainloop()
