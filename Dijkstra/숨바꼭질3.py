import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().strip().split())

def get_move_point(point: int, current_time: int) -> dict:
    return {
        point - 1 :  current_time + 1, 
        point + 1 : current_time + 1,  
        point * 2 : current_time 
        }

times = [float('inf') for _ in range(2000001)]
will_visit_point = []

times[N] = 0
heapq.heappush(will_visit_point, [0,N])

while will_visit_point:
    current_time, current_point = heapq.heappop(will_visit_point)
    
    if current_time > times[current_point]:
        continue
    
    for next_point, next_time in get_move_point(current_point, current_time).items():
        if next_point >= 0 and next_point <= 200000 and times[next_point] > next_time:
            times[next_point] = next_time
            heapq.heappush(will_visit_point, [next_time, next_point])

print(times[K])
