
from game_object import Game

game = Game()

print("command line test")
print(
    "The following commands are available",
    "Get Heros"
)

curr_input = input()
while curr_input != 'quit':
    if (curr_input == "Get Heros"):
        print(game.Get_Heros())
    curr_input = input()
