import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("Maroon")
screen.setup(width=600, height=600)
screen.tracer(0)
dustin_the_turtle  = Player()
building_car_set  = CarManager()
game_level_board = Scoreboard((-280 , 280))
game_over_board= Scoreboard((-40 ,0))




screen.onkeypress(dustin_the_turtle.move_forward , "Up" )
screen.listen()

round = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    round += 1
    if round % 6 == 0 :
        building_car_set.create_a_car()

    building_car_set.move_car()

    for i in building_car_set.all_cars :
        if dustin_the_turtle.distance(i) < 20 :
            dustin_the_turtle.reset_position()
            game_level_board.reset_score()
    if dustin_the_turtle.ycor() == -280 :
        dustin_the_turtle.forward(5)
        game_level_board.game_level()
    if dustin_the_turtle.ycor() > 280:
        dustin_the_turtle.reset_position()
        building_car_set.increase_the_speed()

screen.exitonclick()