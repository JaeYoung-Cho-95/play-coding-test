import sys
from collections import deque

def dfs_or_bfs(graph, V, flag):
    start_points = deque(sorted(graph[V]))
    visited_points = [False for _ in range(N+1)]
    visited_points[V] = True
    result = f"{V}"
    
    while True:
        try:
            start_point = start_points.popleft()
        except:
            break
        
        if not visited_points[start_point]:
            visited_points[start_point] = True
            
            if flag:
                start_points = deque(sorted(graph[start_point])) + start_points
            else:
                start_points = start_points + deque(sorted(graph[start_point]))
            result += f" {start_point}"
        
        if len(start_points) == 0:
            break

    print(result.rstrip())

N,M,V = map(int, sys.stdin.readline().strip().split())
graph = {x : deque([]) for x in range(1,N+1)}

for _ in range(M):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs_or_bfs(graph,V,True)
dfs_or_bfs(graph,V,False)