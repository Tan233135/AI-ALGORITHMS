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