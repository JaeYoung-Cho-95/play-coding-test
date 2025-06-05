import heapq
import sys

input = sys.stdin.readline

count_node, count_edge = map(int, input().strip().split())
start_node = int(input().strip())

graph = {x : {} for x in range(1, count_node + 1)}

for _ in range(count_edge):
    st_node, ed_node, weight = map(int, input().strip().split())
    
    already_weight = graph[st_node].get(ed_node, None)
    
    if not already_weight:
        graph[st_node][ed_node] = weight
    else:
        if already_weight > weight:
            graph[st_node][ed_node] = weight

distances = [0] + [float('inf') for _ in range(count_node)]
distances[start_node] = 0
will_visit_nodes = []
heapq.heappush(will_visit_nodes, [0, start_node])

while will_visit_nodes:
    start_weight, start_node = heapq.heappop(will_visit_nodes)
    
    if distances[start_node] < start_weight:
        continue
    
    for node, weight in graph[start_node].items():
        temp_distance = start_weight + weight
        
        if distances[node] > temp_distance:
            distances[node] = temp_distance
            heapq.heappush(will_visit_nodes, [temp_distance, node])
            

for distance in distances[1:]:
    print(distance) if distance != float('inf') else print("INF")