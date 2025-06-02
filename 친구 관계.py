"""
문제
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
"""

# # 데이터가 입력될 때마다 트리에 넣어준다.
# # 친구1, 친구2 를 입력받는다.
# # 친구1, 친구2 에 연결된 노드들을 방문할 리스트로 담아놓는다.
# # 방문하지 않은 친구는 False 로 바꾸면서 cnt += 1 을 한다.

# import sys
# from collections import deque

# input = sys.stdin.readline

# for _ in range(int(input().strip())):
#     tree = {}
#     caseNum = int(input().strip())
#     for _ in range(caseNum):
#         friend_1, friend_2 = input().strip().split()
        
#         try:
#             tree[friend_1].append(friend_2)
#         except:
#             tree[friend_1] = deque([friend_2])
            
#         try:
#             tree[friend_2].append(friend_1)
#         except:
#             tree[friend_2] = deque([friend_1])
        
#         will_visit = deque()
#         will_visit.extend(tree[friend_1])
#         will_visit.extend(tree[friend_2])
#         already_visit = {}
        
#         while True:
#             if not len(will_visit):
#                 break
            
#             friend = will_visit.pop()
            
#             try:
#                 if already_visit[friend]:
#                     continue
#             except:
#                 already_visit[friend] = True
#                 will_visit.extend(tree[friend])
            
#         print(len(already_visit))


# 1. 테스트 케이스 수를 입력받는다.
# 2. 테스트 케이스의 친구 관계의 수를 입력받는다.
# 3. 연결이 될 수 있는 tree 구조를 할당해놓는다.
# 4. 각 이름별로 어디에 포함되어있는지 저장할 수 있는 hashtable 도 할당한다.
# 5. 친구 관계인 이름 2개를 입력받는다.
# 6. 친구 1이 포함된 node 가 있는지 찾는다.
# 7. 친구 2가 포함된 node 가 있는지 찾는다.
# 8-1. 친구 1만 포함된 node 가 있다면, 해당 node 에 연결
# 8-2. 친구 2만 포함된 node 가 있다면, 해당 node 에 연결
# 8-3. 친구1, 2 모두 포홤된 node 가 있다면 2개의 node 를 연결해주기.
# 8-4. 친구1, 2 모두 연결될 node 가 없다면, 새로운 index 에 연결


import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input().strip())

def x(data):
    index_hash[friend_1] = data
    index_hash[friend_2] = data
    print(len(union_tree[data]))
    
for _ in range(test_case):
    friend_case = int(input().strip())
    connect_index = 1
    union_tree, index_hash = {}, {}
    
    for _ in range(friend_case):
        friend_1, friend_2 = input().strip().split()
    
        friend_1_index = index_hash.get(friend_1, None)
        friend_2_index = index_hash.get(friend_2, None)
        
        if not friend_1_index and not friend_2_index:
            union_tree[connect_index] = deque([friend_1, friend_2])
            x(connect_index)
            connect_index += 1
        
        elif friend_1_index and not friend_2_index:
            union_tree[friend_1_index].append(friend_2)
            x(friend_1_index)
        
        elif not friend_1_index and friend_2_index:
            union_tree[friend_2_index].append(friend_1)
            x(friend_2_index)
        
        elif friend_1_index != friend_2_index:
            union_tree[friend_1_index].extend(union_tree[friend_2_index])
            for name in list(union_tree[friend_2_index]):
                index_hash[name] = friend_1_index
            del union_tree[friend_2_index]
            x(friend_1_index)
            
        else:
            print(len(union_tree[friend_1_index]))

