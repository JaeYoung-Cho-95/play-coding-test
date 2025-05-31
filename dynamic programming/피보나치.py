x = [1,1]
n = int(input())

for i in range(2, n):
    x.append(x[i-1] + x[i-2])
    
print(x[-2])