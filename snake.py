import turtle
import time
import random 
delay = 0.1
#score
score = 0
high_score = 0

root = turtle.Screen()
root.title("Snake Game")
root.bgcolor('black')
root.setup(600,600)
root.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction ="stop"

#===food===
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)

segments = []

#border
border=turtle.Turtle()
border.hideturtle()
border.penup()
border.color("white")
border.goto(-290,290)
border.pendown()
border.forward(600)
border.right(90)
border.forward(600)
border.right(90)
border.forward(600)
border.right(90)
border.forward(600)
border.right(90)
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,320)
pen.write("score: 0 high score: 0",align="center",font=("courier",24,"normal"))
#function
def go_up():
    if head.direction !="down":
        head.direction = "up"
    
def go_down():
    if head.direction !="up":
        head.direction = "down"

def go_left():
    if head.direction !="right":
        head.direction = "left"

def go_right():
    if head.direction !="left":
        head.direction = "right"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keyboard bindings
root.listen()
root.onkeypress(go_up,'w')
root.onkeypress(go_down,'s')
root.onkeypress(go_left,'a')
root.onkeypress(go_right,'d')

#main game loop
while True:
    root.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"
        for segment in segments:
            segment.goto(1000,1000)
            segment.clear()
        score = 0
        delay=0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
        score, high_score), align="center", font=("candara", 24, "bold"))
#check for food collection
    if head.distance(food)<20:
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.goto(x,y)
        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color('brown')
        new_segment.penup()
        segments.append(new_segment)
        delay-=0.001
        #increase the score
        score +=5 

        if score>high_score:
            heigh_score=score

        pen.clear()
        pen.write("score: {} high score : {}".format(score,heigh_score),align="center",font=("courier",24,"normal"))

    #move segment
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
#check for body segment
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.direction ="stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear() 
    time.sleep(delay)
root.mainloop()