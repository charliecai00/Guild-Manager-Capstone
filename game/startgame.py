# Useful local testing script for game_object
# Informal file; created for convenience

from game.game_object import Game

game = Game()

curr_input = input()
while curr_input != 'quit':
    if curr_input == "test":
        game.Add_Heros(10, 'mage')
        game.Hire_Hero(0)
        # game.Add_Party_With_Heros(["0"])
        game.Fire_Hero(0)
        # game.Disband_Party(0)
        print('hired heros:', game.guild.hired_heros_dic)
        print('parties: ', game.guild.party_dic)
    curr_input = input()
