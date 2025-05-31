x = int(input())
num_list = list(map(int, input().split()))
result = {
    0 : 1,
    1 : 3
}

for i in range(2,x):
    temp = result[i-2] + num_list[i]
    if temp > result[i-1]:
        result[i] = temp
    else:
        result[i] = result[i-1]
        
print(result[x-1])