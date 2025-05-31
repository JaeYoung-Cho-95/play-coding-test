import sys
from collections import deque
input = sys.stdin.readline
# last_num = int(input())
# wait_list = deque((map(int, input().split(" "))))
temp_list = deque()
count = 1

last_num = 5 
wait_list = deque([2,1,5,3,4])


while True:
    if len(wait_list) > 0:
        wait_num = wait_list.popleft()
    else:
        wait_num = -1
        
    if len(temp_list) > 0:
        temp_num = temp_list.pop()
    else:
        temp_num = -1
    
    if count == wait_num:
        count += 1
        if temp_num != -1:
            temp_list.append(temp_num)
    elif count == temp_num:
        count += 1
        if wait_num != -1:
            temp_list.append(wait_num)
    else:
        if temp_num != -1:
            temp_list.append(temp_num)
        if wait_num != -1:
            temp_list.append(wait_num)
            
    # print("count : ", count)
    # print("wait_num : ", wait_num)
    # print("temp_num : ", temp_num)
    # print("wait_list : ", wait_list)
    # print("temp_list : ", temp_list)
    # print("*"*30)

    if count == last_num:
        print("Nice")
        break
    if len(wait_list) == 0 and temp_list[-1] != count:
        print("Sad")
        break
