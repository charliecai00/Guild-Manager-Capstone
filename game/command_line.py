
from turtle import done
from game_object import Game

game = Game()

# commands
Heros = "Get Heros"
Hire = "Hire Heros"
List = "List Guild Members"
PartyAdd = "Add To Party"
GetQuest = "Get Quests"
DoQuest = "Do Quest"

print("command line test")
print(
    "The following commands are available:\n",
    Heros,
    Hire,
    List,
    PartyAdd,
    GetQuest,
    DoQuest,
    sep=', '
)

curr_input = input(': ')
while curr_input != 'quit':
    if (curr_input == Heros):
        print(game.Get_Heros())
    elif (curr_input == Hire):
        hired_hero = input("Name of hero you want to hire: ")
        if not game.Hire_Hero(hired_hero):
            print("Could not hire hero, out of money")
    elif (curr_input == List):
        print(game.Guild_Status())
    elif (curr_input == PartyAdd):
        party_name = input("Enter party name: ")
        i = 0
        loop_done = False
        hero_list = []
        print("Enter up to five hero names (or type 'done' to stop)")
        while i < 5 and not loop_done:
            curr_hero = input()
            if curr_hero != 'done':
                hero_list.append(game.Find_Hero(curr_hero))
            else:
                loop_done = True
        if len(hero_list) != 0:
            game.Add_Party(party_name, hero_list)
            print("party added")
        else:
            print("input missing, no party added")
    elif (curr_input == GetQuest):
        print(game.Get_Quest())
    elif (curr_input == DoQuest):
        quest_name = input("Enter quest name: ")
        party_name = input("Enter party name: ")
        result = game.Do_Quest(quest_name, party_name)
        if result:
            print("{} completed the quest!".format(party_name))
        else:
            print("{} failed".format(party_name))
    curr_input = input(': ')
