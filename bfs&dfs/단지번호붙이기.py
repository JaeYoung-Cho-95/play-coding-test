from collections import deque
from typing import List, Tuple

def create_already_visited(N: int, apart_list: List[List[int]]) -> List[List[bool]]:
    already_visited = [[False for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if apart_list[y][x] == 0:
                already_visited[y][x] = True
    return already_visited


def create_apart_list(N: int) -> List[List[int]]:
    apart_list = []
    for _ in range(N):
        apart_list.append(list(map(int, input())))
    return apart_list


def dfs(y: int, x: int, N: int, already_visited : List[List[bool]]) -> Tuple[int, List]:
    cnt = 1
    will_visit = deque([[y,x]])
    already_visited[y][x] = True
    
    while will_visit:
        y, x = will_visit.popleft()
        
        for next_step in extracted_next_step(y, x, N):
            next_y, next_x = next_step
            
            if not already_visited[next_y][next_x]:
                cnt += 1
                already_visited[next_y][next_x] = True
                will_visit.append([next_y, next_x])
    
    return cnt, already_visited


def extracted_next_step(y: int ,x: int ,N: int) -> List[List[int]]:
    can_moves = [[1,0],[-1,0],[0,1],[0,-1]]
    next_steps = []
    for can_move in can_moves:
        move_y = y + can_move[0]
        move_x = x + can_move[1]
        
        if move_y < 0 or move_y >= N: continue
        if move_x < 0 or move_x >= N: continue
        
        next_steps.append([move_y, move_x])
    return next_steps


N = int(input())
apart_list = create_apart_list(N)
already_visited = create_already_visited(N, apart_list)

result = []
for y in range(N):
    for x in range(N):
        if not already_visited[y][x]:
            cnt, already_visited = dfs(y,x,N, already_visited)
            result.append(cnt)
            
print(len(result))
for cnt in sorted(result):
    print(cnt)
            