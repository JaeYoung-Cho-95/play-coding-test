"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

N = int(input())
if N == 1: print(0)
elif N == 2 or N == 3: print(1)
else:
    data = [0 for _ in range(N+1)]
    data[2], data[3] = 1,1
    for i in range(4, N+1):
        data[i] = data[i-1] + 1
        if i % 2 == 0:
            data[i] = min(data[i],data[int(i/2)] + 1) if data[i] else data[int(i/2)] + 1
        if i % 3 == 0:
            data[i] = min(data[int(i/3)] + 1, data[i]) if data[i] else data[int(i/3)] + 1
    print(data[N])