COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.new_distance = STARTING_MOVE_DISTANCE
    def create_a_car(self) :
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1 , 2)
        colour = random.choice(COLORS)
        new_car.color(colour)
        starting_ycor = random.randint(-220,220)
        new_car.penup()
        new_car.goto(320 , starting_ycor)
        self.all_cars.append(new_car)



    def move_car(self) :
        for car in self.all_cars :
            new_xcor =  car.xcor() - self.new_distance
            car.goto(new_xcor , car.ycor())


    def increase_the_speed(self):
        self.new_distance += MOVE_INCREMENT