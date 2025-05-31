import sys
from collections import deque

N,M = map(int, input().split())
graph = []
length = []
for _ in range(N):
    graph.append(sys.stdin.readline().strip())
    length.append([0 for _ in range(M)])


def check_inside(a,b) -> bool:
    if 0 <= a and a < N and 0 <= b and b < M and int(graph[a][b]):
        return True
    return False

def calculate_distance(length, row, col, distance, start_points):
    if length[row][col] == 0:
        length[row][col] = distance + 1
        start_points.append([row,col])
    elif length[row][col] > distance + 1:
        length[row][col] = distance + 1
    
    return length, start_points
    

start_points = deque([[0,0]])
length[0][0] = 1

while True:
    start_row, start_col = start_points.popleft()
    distance = length[start_row][start_col]
    
    next_row_1, next_col_1 = start_row - 1, start_col 
    next_row_2, next_col_2 = start_row, start_col - 1
    next_row_3, next_col_3 = start_row + 1, start_col
    next_row_4, next_col_4 = start_row, start_col + 1
    
    if check_inside(next_row_1, next_col_1):
        length, start_points = calculate_distance(length, next_row_1, next_col_1, distance, start_points)
    
    if check_inside(next_row_2, next_col_2):
        length, start_points = calculate_distance(length, next_row_2, next_col_2, distance, start_points)
        
    if check_inside(next_row_3, next_col_3):
        length, start_points = calculate_distance(length, next_row_3, next_col_3, distance, start_points)
        
    if check_inside(next_row_4, next_col_4):
        length, start_points = calculate_distance(length, next_row_4, next_col_4, distance, start_points)
    
    if len(start_points) == 0:
        break

print(length[N-1][M-1])