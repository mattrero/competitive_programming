
from collections import defaultdict
import sys


# map(int, list1, list2)


# ord('a')
# chr(97)

import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

def distance_path(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)






import queue

class Node:

    def __init__(self, node_id, **kwargs):
        self.node_id = node_id
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __eq__(self, other):
        return self.node_id == other.node_id

    def __hash__(self):
        return hash(self.node_id)

    def __repr__(self):
        d = dict(self.__dict__)
        del d['node_id']
        return str(d)

    def __lt__(self, other):
        # TODO implement this
        return False


class _PathNode:
    def __init__(self, score, node, parent = None):
        self.score = score
        self.node = node
        self.parent = parent

    def __lt__(self, other):
        if self.score == other.score:
            self_path = self.get_path()
            other_path = self.get_path()

            if len(self_path) < len(other_path):
                return True
            if len(self_path) > len(other_path):
                return False

            for n1, n2 in zip(self_path, other.get_path()):
                if n1 == n2:
                    continue
                return n1 < n2
            return False

        return self.score < other.score

    def get_path(self):
        path = [self.node]

        current = self

        while current.parent:
            current = current.parent
            path.insert(0, current.node)

        return path


def solve_a_star(start, goal_or_eval, get_neighbors):
    """

    :param nodes: List of all nodes
    :param start:
    :param goal_or_eval: Either a goal of type Node or a function receiving a _PathNode
    :param get_neighbors: List neighbors of specific node : (score, neighbor)
    :return:
    """

    if type(goal_or_eval) is Node:
        eval_goal = lambda n: n.node == goal_or_eval
    else:
        eval_goal = goal_or_eval

    q = queue.PriorityQueue()
    q.put(_PathNode(0, start))

    done = set()

    while not q.empty():
        current = q.get() #type: _PathNode

        if eval_goal(current):
            return current.get_path()

        if current.node in done:
            continue

        done.add(current.node)

        for add_score, neighbor in get_neighbors(current.node):
            if neighbor not in done:
                q.put(_PathNode(current.score + add_score, neighbor, current))




def bruteforce(start,
                get_neighbors,
                is_valid_path = lambda node_path:len(node_path.get_path()) == len(set(node_path.get_path())),
                is_first_best = lambda a,b: a.score < b.score):

    q = queue.Queue()
    q.put(_PathNode(0, start))

    best_path = None

    while not q.empty():
        current = q.get() #type: _PathNode

        if is_first_best(current, best_path):
            best_path = current

        for add_score, neighbor in get_neighbors(current.node):
            path = _PathNode(current.score + add_score, neighbor, current)
            if is_valid_path(path):
                q.put(path)

    return best_path
