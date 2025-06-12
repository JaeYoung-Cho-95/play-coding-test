import sys
from collections import deque

input = sys.stdin.readline

def can_move_points(row: int, column: int) -> list:
    next_points = deque([[row + 1, column], [row, column + 1], [row  - 1, column], [row , column - 1]])
    for _ in range(4):
        next_row, next_column = next_points.popleft()
        if next_row >= j or next_row < 0 or next_column >= i or next_column < 0: continue
        elif tomato_map[next_row][next_column] != 0: continue
        next_points.append([next_row, next_column])
    
    return next_points

def result(tomato_map: list) -> int:
    max_value = 0
    for i_tomato_map in tomato_map:
        max_value = max(max(i_tomato_map), max_value)
        if 0 in i_tomato_map:
            return -1
    return max_value-1

i, j = map(int, input().strip().split())
tomato_map = deque([])
will_visit = deque([])

for row in range(j):
    row_tomato = deque(list(map(int, input().strip().split())))
    tomato_map.append(deque([]))
    
    for column in range(i):
        temp = row_tomato[column]
        tomato_map[row].append(temp)
        
        if temp == 1:
            will_visit.append([row, column])


while will_visit:
    row, column = will_visit.popleft()
    next_points = can_move_points(row, column)
    
    for next_row, next_column in next_points:
        tomato_map[next_row][next_column] = tomato_map[row][column] + 1
    
    will_visit.extend(deque(next_points))

print(result(tomato_map))