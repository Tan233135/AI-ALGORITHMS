import heapq

def dijkstra(graph, start):
    # Store shortest distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue (distance, node)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Check neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example Graph
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'D': 1},
    'C': {'B': 2, 'D': 5},
    'D': {}
}

# Run algorithm
result = dijkstra(graph, 'A')

print(result)