
FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self , location):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(location)
        self.level = 1
        self.highest_level = 1

    def game_level(self):
        self.clear()
        with open("Highest_Level.txt", mode="r") as file:
            data = int(file.read())
            if data > self.level :
                self.highest_level = data

            if data < self.level :
                self.highest_level = self.level
                with open("Highest_Level.txt", mode="w") as f:
                    f.write(f"{self.highest_level}")
        self.write(arg = f"Level = {self.level} Highest Level = {self.highest_level}"  , font = "FONT")
        self.level += 1


    def reset_score(self):
        self.clear()
        self.level -= 1



