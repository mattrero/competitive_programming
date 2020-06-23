from queue import PriorityQueue

class AStarGraph:

    def __init__(self):
        self.start = None
        self.goal = None

    def init(self, start, goal):
        self.start = start
        self.goal = goal

    def get_start(self):
        return self.start

    def is_goal(self, node) -> bool:
        return node == self.goal

    def neighbors(self, node, came_from, current_cost):
        """
        :return: List or generator of nodes
        """

        raise NotImplemented()

    def cost(self, current_node, next_node) -> float:
        raise NotImplemented()

    def heuristic_cost_to_goal(self, node) -> float:
        raise NotImplemented()


def a_star_search(graph: AStarGraph):
    queue = PriorityQueue()

    start = graph.get_start()

    queue.put(start, 0)

    came_from = {start: None}
    cost_so_far = {start: 0}

    while not queue.empty():
        current = queue.get()

        if graph.is_goal(current):
            return current, came_from, cost_so_far

        for next in graph.neighbors(current, came_from, cost_so_far[current]):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                came_from[next] = current
                queue.put(next, new_cost + graph.heuristic_cost_to_goal(next))

    return None, came_from, cost_so_far
