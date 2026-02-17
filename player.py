STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("YellowGreen")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

#Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress
# to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

    def move_forward(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(0 , new_ycor)

    def reset_position(self):
        self.goto(STARTING_POSITION)