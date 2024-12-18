from turtle import Turtle, Screen
from random import randint



is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange", "yellow", "green", "blue", "purple"]
y_positions= [-100,-60,-20,20,60,100]
turtle_list = []



for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    turtle_list.append(new_turtle)




if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in turtle_list:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
                
        random_distance = randint(0,10)
        turtle.forward(random_distance)

            
    


    




screen.exitonclick()