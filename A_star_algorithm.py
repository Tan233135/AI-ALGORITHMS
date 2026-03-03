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

import math
import heapq

class cell:
    def __init__(self):
        self.parent_i = 0 #parent cell's row index
        self.parent_j = 0 #parent cell's column index
        self.f = float('inf') #total cost of the cell = g+h
        self.g = float('inf') #cost from start to this cell
        self.h = 0 #Heuristic cost from this cell to destination

ROW = 9
COL = 10

def is_valid(row,col):
    return (row>=0) and (row<ROW) and (col>=0) and (col<COL)

def is_unblocked(grid,row,col):
    return grid[row][col] ==1

def is_destination(row,col,dest):
    return row == dest[0] and col == dest[1]

def calculate_h_value(row,col,dest):
    return ((row-dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

def trace_path(cell_details,dest):
    print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row,col))
        temp_row =  cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col
    path.append((row,col))
    path.reverse()
    for i in path:
        print(" -> ",i,end=" ")
    print()
    