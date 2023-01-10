# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from random import randint, randrange
from typing import Tuple
from game.object_classes.quest import Quest
from game.object_classes.hero import Hero
from game.object_classes.challenge import Challenge


class Party:
    def __init__(self,
                 new_id: int,
                 new_hero_list: list = [],
                 name: str = "test") -> None:
        self.id = new_id
        self.hero_list = new_hero_list
        self.name = name
        self.best_stats = {}
        self.mean_stats = {}
        self.Calc_Stats()

    def __str__(self) -> str:
        # heros = [h.id for h in self.hero_list]
        return "<<Party named '{}' with Heros: {}>>".format(self.name, self.hero_list)

    def __repr__(self):
        return str(self)

    def __eq__(self, __o: object) -> bool:
        return __o.id == self.id

    # if any heroes in the party are still alive
    def Is_Alive(self) -> bool:
        for h in self.hero_list:
            if h.alive:
                return True
        return False

    def Add_Hero(self, new_hero: Hero) -> bool:
        try:
            self.hero_list.append(new_hero)
            self.Calc_Stats()
            return True
        except Exception:
            return False

    def Remove_Hero(self, hero_id: int) -> bool:
        try:
            for i in range(len(self.hero_list)):
                if self.hero_list[i].id == hero_id:
                    self.hero_list.pop(i)
                    self.Calc_Stats()
                    return True
            return False
        except Exception:
            return False

    def Calc_Stats(self) -> None:
        stat_names = ["STR", "CON", "DEX", "WIS", "INT", "CHA"]
        # best stats
        for h in self.hero_list:
            for s in stat_names:
                if s in self.best_stats:
                    if self.best_stats[s] < h.stats[s]:
                        self.best_stats[s] = h.stats[s]
                else:
                    self.best_stats[s] = h.stats[s]
        # mean stats
        for h in self.hero_list:
            for s in stat_names:
                if s in self.mean_stats:
                    self.mean_stats[s] += h.stats[s]
                else:
                    self.mean_stats[s] = h.stats[s]
        for s in stat_names:
            if len(self.hero_list) != 0:
                self.mean_stats[s] = self.mean_stats[s] // len(self.hero_list)

    def Get_Random_Hero(self) -> Hero:
        return self.hero_list[randint(0, len(self.hero_list) - 1)]

    # quest functions
    def Complete_Quest(self, quest: Quest) -> Tuple[list, bool]:
        quest.start(self.best_stats, self.mean_stats)
        report = []
        while self.Is_Alive() and not quest.done:
            curr_node = quest.next_node()
            result = self.Take_Challenge(curr_node.challenge)
            if result:  # success
                report.append(curr_node.challenge.success_message)
                quest.succeed_node(curr_node)
            else:   # failure
                report.append(curr_node.challenge.fail_message)
                quest.fail_node(curr_node)
        return report, self.Is_Alive()

    def Take_Challenge(self, challenge: Challenge) -> bool:
        skill = challenge.Get_Skill()
        if challenge.type == "Random":
            curr_hero = self.Get_Random_Hero()
            return curr_hero.Test_Skill(skill)
        elif challenge.type == "Best":
            roll = randrange(99)
            return roll <= self.best_stats[skill]
        elif challenge.type == "Mean":
            roll = randrange(99)
            return roll <= self.mean_stats[skill]
