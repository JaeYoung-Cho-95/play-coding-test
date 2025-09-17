from collections import deque

def solution(N, board):
    answer = []
    target_points = get_target_points(board)
    
    for st_x in range(N):
        for st_y in range(N):
            temp = []
            for ed_x, ed_y in target_points:
                min_distance_to_target = get_minimum_distance(st_x, st_y, ed_x, ed_y ,N)
                temp.append(min_distance_to_target)
            print(temp)
            print(min(temp))
    return answer

def get_target_points(board):
    target_points = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "G":
                target_points.append([i,j])

    return target_points


def get_minimum_distance(st_x, st_y, ed_x, ed_y, N):
    start_points = deque([[st_x, st_y]])
    distances = [[0 for _ in range(N)] for _ in range(N)]
    distances[st_x][st_y] = 0

    while start_points:
        st_x, st_y = start_points.popleft()
        current_distance = distances[st_x][st_y]
        if st_x == ed_x and st_y == ed_y:
            return current_distance
        
        next_points = get_next_points(st_x, st_y, N)
        
        for nt_x, nt_y in next_points:
            if not distances[nt_x][nt_y] or distances[nt_x][nt_y] > current_distance + 1:
                distances[nt_x][nt_y] = current_distance + 1
                start_points.append([nt_x, nt_y])
    

def get_next_points(st_x, st_y, N):
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    next_points = []
    for x,y in move:
        nt_x = st_x + x
        nt_y = st_y + y

        if nt_x < 0 or nt_x >= N:
            continue
        
        if nt_y < 0 or nt_y >= N:
            continue

        next_points.append([nt_x, nt_y])
    
    return next_points

