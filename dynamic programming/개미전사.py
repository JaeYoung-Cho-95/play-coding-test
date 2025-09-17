def solution(store):
    for i in range(2, len(store)):
        store[i] = max(store[i] + store[i -2], store[i - 1])
    return store[-1]

store = [1,3,1,5]
print(solution(store))