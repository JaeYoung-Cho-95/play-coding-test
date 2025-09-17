n = int(input())
data = [0, 0, 1, 1, 2] + [0 for _ in range(5, n+1)]

for i in range(5, n+1):
    case1 = data[i-1] + 1
    case2 = data[(int(i/2))] + 1 if not i % 2 else float('inf')
    case3 = data[(int(i/3))] + 1 if not i % 3 else float('inf')
    
    data[i] = min([case1, case2, case3])

print(data[n])