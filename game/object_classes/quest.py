# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import random
from random import randint
from game.object_classes.challenge import Challenge
from game.startgame import game


class Quest:
    class Node:
        def __init__(self,
                     challenge,
                     children=[],
                     stat=None,
                     terminal=False) -> None:
            self.challenge = challenge
            self.check_stat = stat      # currently not used
            self.children = children
            self.terminal = terminal
            self.parent = None
            self.done = False
            self.depth = 0

        def add_child(self, new_node) -> None:
            new_node.parent = self
            self.children.append(new_node)

        def check_children(self, stats: dict = None) -> list:
            ret_lst = []
            for c in self.children:
                if c.check_stat is not None:
                    if stats is not None:
                        pass  # test party stat
                else:
                    ret_lst.append(c)
            return ret_lst

        def resolve(self, party) -> bool:
            result = party.Take_Challenge(self.challenge)
            if not self.terminal:
                self.done = True
            return result

        def __str__(self) -> str:
            return "|Challenge: {}, End?: {}|".format(
                self.challenge,
                self.terminal)

    # leave default constructor for the MAP
    def __init__(self) -> None:
        self.name = "A Great Quest"
        self.done = False
        self.curr_nodes: list[self.Node] = []
        self.nodes_master_list: list[self.Node] = []
        self.root = self.generate_nodes()
        self.curr_nodes.append(self.root)
        self.nodes_master_list.append(self.root)
        self.best_p_stats = {}  # local party stats
        self.mean_p_stats = {}  # overriden for each party
        self.location = random.choice(list(game.map.locations.values()))

    def __str__(self) -> str:
        info = self.get_info()
        return "Name: {}, {}".format(info[0], info[1:])

    def get_info(self) -> list:
        ret_list = [self.name]
        for c in self.nodes_master_list:
            ret_list.append(str(c))
        return ret_list

    def generate_nodes(self) -> Node:
        stat_names = ["STR", "CON", "DEX", "WIS", "INT", "CHA"]
        curr_layer: list[self.Node] = []
        root = self.Node(Challenge(stat_names[randint(0, len(stat_names) - 1)]))
        self.root = root
        curr_layer.append(root)
        max_depth = 5
        while len(curr_layer) != 0:
            curr_node: self.Node = curr_layer.pop(0)
            num_of_children = randint(0, 3)
            if num_of_children != 0 and curr_node.depth < max_depth:
                for i in range(num_of_children):
                    new_node = self.Node(Challenge(
                        stat_names[randint(0, len(stat_names) - 1)]))
                    new_node.parent = curr_node
                    new_node.depth = new_node.parent.depth + 1
                    curr_node.children.append(new_node)
                    curr_layer.append(new_node)
            else:
                curr_node.terminal = True
            self.nodes_master_list.append(curr_node)
        for n in curr_layer:
            n.terminal = True
            self.nodes_master_list.append(n)
        return root

    def start(self, best_stats: dict, mean_stats: dict) -> None:
        self.best_p_stats = best_stats.copy()
        self.mean_p_stats = mean_stats.copy()
        for n in self.nodes_master_list:
            n.done = False

    def succeed_node(self, done_node: Node) -> None:
        if done_node.terminal:
            self.done = True
        self.curr_nodes.remove(done_node)
        for c in done_node.check_children(self.best_p_stats):
            self.curr_nodes.append(c)

    def fail_node(self, fail_node: Node) -> None:
        # recheck parents nodes
        for c in fail_node.parent.check_children(self.mean_p_stats):
            if c not in self.curr_nodes:
                self.curr_nodes.append(c)

    def next_node(self) -> Node:
        for n in self.curr_nodes:
            if not n.done:
                return n
