'''Uniform Cost Search(UCS)
1. UCS is an uninformed search algorithm.
2. Finds the least-cost path from a start node to a goal node 
   in a weighted graph.
3. Variant of Dijksta's algorithm.
4. Guarantees optimal solution if step costs are non-negative.
5. Expresses nodes with the lowest cumulative cost first.
6. Uses priority queue to manage nodes.'''

import heapq
import networkx as nx
import matplotlib.pyplot as plt
#The "heapq" is used for the priotity queue
#The "networkx" is used for analyze and manipulate complex netowkrs
#The "matplotlib" is used for graph visualization

#The uniform cost function
def uniform_cost_function(graph,start,goal):
    priority_queue=[(0,start)]
    visited = {start:(0,None)} #dictionary to store the cost of the shortest path to each node
    while priority_queue:
        #Pop the node with the lowest cost from the priority queue
        current_cost,current_node=heapq.heappop(priority_queue)
        #if we reached the goal, return the total cost and the path
        if current_node == goal:
            return current_cost,reconstruct_path(visited,start,goal)
        for neighbor,cost in graph[current_node]:
            total_cost=current_cost+cost
            if neighbor not in visited or total_cost<visited[neighbor][0]:
                visited[neighbor]=(total_cost,current_node)
                heapq.heappush(priority_queue,(total_cost,neighbor))
    return None

def reconstruct_path(visited,start,goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1] #get the parent node
    path.reverse()
    return path

def visualization_graph(graph,path=None):
    G=nx.DiGraph()
    for node,edges in graph.items():
        for neighbor,cost in edges:
            G.add_edge(node,neighbor,weight=cost)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8,6))
    nx.draw(G,pos,with_labels=True,node_color='lightblue',node_size=2000,font_size=15,font_weight='bold',edge_color='grey')
    labels=nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=12)
    if path:
        path_edges=list(zip(path,path[1:]))
        nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='red',width=2.5)
    plt.title("Uniform Cost Search Path Visualization")
    plt.show()

