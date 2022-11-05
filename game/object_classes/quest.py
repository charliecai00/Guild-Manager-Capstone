
class Quest:
    class Node:
        def __init__(self,
                     challenge,
                     children=[],
                     stat=None,
                     terminal=False) -> None:
            self.challenge = challenge
            self.check_stat = stat
            self.children = children
            self.terminal = terminal
            self.parent = None
            self.done = False

        def add_child(self, new_node):
            new_node.parent = self
            self.children.append(new_node)

        def check_children(self, stats: dict = None):
            ret_lst = []
            for c in self.children:
                if c.check_stat is not None:
                    if stats is not None:
                        pass  # test party stat
                else:
                    ret_lst.append(c)
            return ret_lst

        def resolve(self, party):
            result = party.Take_Challenge(self.challenge)
            if not self.terminal:
                self.done = True
            return result

    # leave default constructor for the MAP
    def __init__(self) -> None:
        self.done = False
        self.root = None    # Quest.Node(Challenge)
        self.curr_nodes = [self.root]
        self.nodes_master_list = []
        self.best_p_stats = {}  # local party stats
        self.mean_p_stats = {}  # overriden for each party

    def generate_nodes(self):
        pass    # TODO: a system to generate nodes

    def start(self, best_stats: dict, mean_stats: dict) -> None:
        self.best_p_stats = best_stats.copy()
        self.mean_p_stats = mean_stats.copy()
        for n in self.nodes_master_list:
            n.done = False

    def succeed_node(self, done_node: Node):
        if done_node.terminal:
            self.done = True
        self.curr_nodes.remove(done_node)
        for c in done_node.check_children(self.best_p_stats):
            self.curr_nodes.append(c)

    def fail_node(self, fail_node: Node):
        # recheck parents nodes
        for c in fail_node.parent.check_children(self.mean_p_stats):
            if c not in self.curr_nodes:
                self.curr_nodes.append(c)

    def next_node(self) -> Node:
        for n in self.curr_nodes:
            if not n.done:
                return n
