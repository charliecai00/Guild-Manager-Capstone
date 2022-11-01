
from random import randint, randrange
from game.object_classes.quest import Quest


class Party:
    def __init__(self, new_id, new_hero_list=[], name="test") -> None:
        self.id = new_id
        self.hero_list = new_hero_list
        self.name = name
        self.best_stats = {}
        self.mean_stats = {}
        self.Calc_Stats()

    def __str__(self) -> str:
        hero_names = [h.name for h in self.hero]

        return "Party: {}, Heros: {}".format(self.name, hero_names)

    def __repr__(self) -> str:
        return str(self)

    # if any heroes in the party are still alive
    def Is_Alive(self):
        for h in self.hero_list:
            if h.alive:
                return True
        return False

    def Add_Hero(self, new_hero):
        self.hero_list.append(new_hero)
        self.Calc_Stats()

    def Calc_Stats(self):
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
            self.mean_stats[s] = self.mean_stats[s] // len(self.hero_list)

    def Take_Challenge(self, challenge):
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

    def Get_Random_Hero(self):
        return self.hero_list[randint(0, len(self.hero_list)-1)]

    def Complete_Quest(self, quest: Quest) -> list:
        report = quest.resolve(self)
        return report
