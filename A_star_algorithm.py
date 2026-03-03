'''A* Search algorithm is one of the best and popular technique used in path-finding and graph traversals.

Unlike other traversal techniques A* algorithm has "brains". What it means is that it is really a 
smart algorithm which separates it from the other conventional algorithms. This fact is celared
in detial in below sections. And it is also worth mentioning that many games and web-based maps use
this algorithm to find the shortest path very efficiently.

Algorithm:
1. Initialize the open list.
2. Initialize the closed list.
3. While the open list is not empty
   a) find the node with the least f on the open list,
      call it "q"
   b) pop q off the open list
   c) generate q's 8 successors and set their parents to q
   d) for each successor
      i) if successor if the goal, stop search
      ii) else, compute the g and h for successor
           successor.g = q.g + distance between successor and q
           successor.h = distance from goal to successor.
           successor.f = successor.g + successor.h
      iii) if a node with the same position as successor is in the OPEN 
           list which has lower f than successor, skip this successor
      iv) if a node with the same position as successor is in the CLOSED list
          which has a lower f than successor, skip this successor otherwise, add 
          the node to the open list
    end (for loop)
    e) push q on the closed list
    end (while loop)'''

import heapq


class Node:
    def __init__(self, position):
        self.position = position   # Can be graph node name OR (x, y) tuple
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f


def a_star(start, goal, get_neighbors, heuristic):
    
    nodes = {}
    
    def get_node(pos):
        if pos not in nodes:
            nodes[pos] = Node(pos)
        return nodes[pos]

    open_list = []
    closed_set = set()

    start_node = get_node(start)
    start_node.g = 0
    start_node.h = heuristic(start, goal)
    start_node.f = start_node.g + start_node.h

    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.position == goal:
            return reconstruct_path(current)

        closed_set.add(current.position)

        for neighbor_pos, cost in get_neighbors(current.position):

            if neighbor_pos in closed_set:
                continue

            neighbor = get_node(neighbor_pos)
            tentative_g = current.g + cost

            if tentative_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor_pos, goal)
                neighbor.f = neighbor.g + neighbor.h

                heapq.heappush(open_list, neighbor)

    return None


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]