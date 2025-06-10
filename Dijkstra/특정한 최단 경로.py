import sys
import heapq

ip = sys.stdin.readline
N, E = map(int, ip().strip().split())

def make_gr(st, ed):
    al_n = gr.get(st)
    
    if al_n: gr[st][ed] = dis
    else: gr[st] = {ed : dis}

def min_dis(start_node : int) -> list:
    will_v = []
    dists = [0] + [float('inf') for _ in range(N)]
    heapq.heappush(will_v, [0, start_node])
    dists[start_node] = 0
    
    while will_v:
        cu_dist, cur_n = heapq.heappop(will_v)
        if cu_dist > dists[cur_n]: continue
        
        for node, dis in gr[cur_n].items():
            temp_dis = cu_dist + dis
            if temp_dis < dists[node]:
                dists[node] = temp_dis
                heapq.heappush(will_v, [temp_dis, node])             
    return dists

gr = {}

for _ in range(E):
    st, ed, dis = map(int, ip().strip().split())
    make_gr(st, ed)
    make_gr(ed, st)

if not E: print(-1)
else:
    node1, node2 = map(int, ip().strip().split()) 
    mi1, mino1, mino2 = min_dis(1), min_dis(node1), min_dis(node2)
    minv = min(mi1[node1] + mino1[node2] + mino2[N], mi1[node2] + mino2[node1] + mino1[N])
    print(minv if minv != float('inf') else -1)
    