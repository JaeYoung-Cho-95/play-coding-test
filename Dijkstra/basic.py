import heapq

graph = {
    "A" : {"B" : 8, "C" : 1, "D" : 2},
    "B" : {},
    "C" : {"B" : 5, "D" : 2},
    "D" : {"E" : 3, "F" : 5},
    "E" : {"F" : 1},
    "F" : {"A" : 5}
}

def dijikstra(graph : dict, start_point : str) -> list:
    distances = { node : float('inf') for node in graph}
    queue = []
    
    distances[start_point] = 0
    heapq.heappush(queue, [distances[start_point], start_point])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue 
        
        for adjacent_node, weight in graph[current_node].items():
            distance = weight + current_distance
            
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                heapq.heappush(queue, [distance, adjacent_node])
        
    return distances

print(dijikstra(graph, "A"))