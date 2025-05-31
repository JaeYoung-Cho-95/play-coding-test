data = [0,1,2]
n = int(input())
if n <= 2: print(data[n])
else:
    for i in range(3,n+1): data.append(data[i-1]+data[i-2])
    print(data[-1] % 10007)