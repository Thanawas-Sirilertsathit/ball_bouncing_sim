import turtle
import random
class Ball:
    def __init__(self,color,pos_x,pos_y,vx,vy,size):
        self.size = size
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vx = vx
        self.vy = vy
    def move_ball(self,canvasheight,canvaswidth):
        self.pos_x+=self.vx
        self.pos_y+=self.vy
        if abs(self.pos_x + self.vx) > (canvaswidth - self.size):
            self.vx = -self.vx
        if abs(self.pos_y + self.vy) > (canvasheight - self.size):
            self.vy = -self.vy
    def draw_circle(self):
    # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.pos_x,self.pos_y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

class Simulate:
    def __init__(self,ball_list):
        self.ball=ball_list
        self.__canvas_width = turtle.screensize()[0]
        self.__canvas_height = turtle.screensize()[1]
    def simulating(self):
        turtle.clear()
        for i in range(len(self.ball)):
            self.ball[i].draw_circle()
            self.ball[i].move_ball(self.__canvas_width,self.__canvas_height)
        turtle.update()
        
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
num_ball=int(input("How many balls do you want? : "))
ball_list=[]
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)

for i in range(num_ball):
    x_initial=random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius)
    y_initial=random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius)
    vx_initial=random.randint(1, 0.01*canvas_width)
    vy_initial=random.randint(1, 0.01*canvas_height)
    ball_color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    my_ball=Ball(ball_color,x_initial,y_initial,vx_initial,vy_initial,ball_radius)
    ball_list.append(my_ball)

screen=Simulate(ball_list)
while True:
    screen.simulating()