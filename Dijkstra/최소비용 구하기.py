import sys
import heapq

input = sys.stdin.readline

N, M = int(input().strip()), int(input().strip())

graph = {}

for _ in range(M):
    start_city, arrive_city, cost = map(int, input().strip().split())
    
    if graph.get(start_city):
        if cost == 0:
            graph[start_city][arrive_city] = cost
        else:
            already_cost = graph[start_city].get(arrive_city, float('inf'))
            if already_cost > cost:
                graph[start_city][arrive_city] = cost
    
    else:
        graph[start_city] = {arrive_city : cost}

    if not graph.get(arrive_city, None):
        graph[arrive_city] = {}
        
start_city, target_city = map(int, input().strip().split())
        
max_city_num = max(graph.keys())
cost = [float('inf')] + [float('inf') for _ in range(max_city_num)]

cost[start_city] = 0
will_visit_node = []
heapq.heappush(will_visit_node, [0, start_city])

while will_visit_node:
    current_cost, current_city = heapq.heappop(will_visit_node)
    
    if cost[current_city] < current_cost:
        continue
    
    for key, value in graph[current_city].items():
        temp_cost = current_cost + value
        
        if cost[key] > temp_cost:
            cost[key] = temp_cost
            heapq.heappush(will_visit_node, [temp_cost, key])
    
print(cost[target_city])