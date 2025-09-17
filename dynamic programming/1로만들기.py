def solution(n):
    min_values = [0,0,1,1,2,1]
    
    if n <= 5:
        return min_values[n]
    
    for i in range(6,n+1):
        temp = []
        if i % 5 == 0: temp.append(i//5)
        if i % 3 == 0: temp.append(i//3)
        if i % 2 == 0: temp.append(i//2)
        min_value = min_values[i-1]
        
        for compare_value in temp:
            min_value = min(min_value, min_values[compare_value])
        
        min_values.append(min_value + 1)
    return min_values[-1]

n = 26
answer = solution(n)
print(answer)
