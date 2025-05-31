import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    temp = deque()
    line = sys.stdin.readline().strip()
    flag = True
    for alpha in line:
        if alpha == "(":
            temp.append("(")
        else:
            if len(temp) == 0 or temp.pop() == ")":
                flag = False
                break
    
    if flag and len(temp) == 0:
        print("YES")
    else:
        print("NO")