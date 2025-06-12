from collections import deque
import sys

N = int(input())
E = int(input())

graph = {x : deque([]) for x in range(1,N+1)}

for _ in range(E):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    

start_points = deque(sorted(graph[1]))
visited_points = [False for _ in range(N+1)]
while True:
    if len(start_points) == 0:
        break
    
    start_point = start_points.popleft()
    
    if not visited_points[start_point]:
        visited_points[start_point] = True
        start_points = start_points + deque(sorted(graph[start_point]))

if not sum(visited_points):
    print(0)
else:
    print(sum(visited_points)-1)