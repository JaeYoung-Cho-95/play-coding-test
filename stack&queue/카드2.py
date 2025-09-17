from collections import deque

n = int(input())
card_deque = deque([x for x in range(1, n+1)])

cnt = 0
while len(card_deque) > 1:
    if cnt % 2 == 0:
        card_deque.popleft()
    else:
        temp = card_deque.popleft()
        card_deque.append(temp)

    cnt += 1

print(card_deque[0])