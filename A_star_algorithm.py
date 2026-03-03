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

def a_star(graph, start, goal, heuristic):
    """
    A* algorithm for graphs
    
    Args:
        graph: dict {node: [(neighbor, cost), ...]}
        heuristic: dict {node: estimated_cost_to_goal}
        start: start node
        goal: goal node
    
    Returns:
        tuple (path, cost) or (None, inf) if no path
    """
    # Priority queue: (f_score, g_score, node, path)
    open_set = [(heuristic[start], 0, start, [start])]
    closed_set = set()
    g_scores = {start: 0}
    
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, g
        
        if current in closed_set:
            continue
            
        closed_set.add(current)
        
        for neighbor, cost in graph.get(current, []):
            if neighbor in closed_set:
                continue
                
            new_g = g + cost
            
            if neighbor not in g_scores or new_g < g_scores[neighbor]:
                g_scores[neighbor] = new_g
                new_f = new_g + heuristic.get(neighbor, float('inf'))
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
    
    return None, float('inf')


# Example usage
if __name__ == "__main__":
    # Graph: adjacency list with costs
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('D', 3), ('E', 4)],
        'C': [('E', 2), ('F', 3)],
        'D': [('G', 4)],
        'E': [('G', 3)],
        'F': [('G', 5)],
        'G': []
    }
    
    # Heuristic: estimated distance to goal 'G'
    heuristic = {
        'A': 6, 'B': 4, 'C': 4, 
        'D': 3.5, 'E': 1, 'F': 1, 'G': 0
    }
    
    path, cost = a_star(graph, 'A', 'G', heuristic)
    
    if path:
        print(f"Path: {' -> '.join(path)}")
        print(f"Cost: {cost}")
    else:
        print("No path found")