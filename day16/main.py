from turtle import Turtle, Screen
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)
#timmy.right(90)
#print(timmy)
#my_screen = Screen()
#my_screen.setup(width=500, height=400)
#print(my_screen.setup)
#my_screen.exitonclick() 

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
print(table)