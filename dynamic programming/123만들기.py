from sys import stdin,  stdout

n = int(stdin.readline())
num_list = []
for _ in range(n):
    num_list.append(int(stdin.readline()))

sorted_num_list = sorted(num_list)
max_num = sorted_num_list[-1]

answer_list = [0, 1, 2, 4, 7]
for i in range(5, max_num + 1):
    answer_list.append(answer_list[i-1] + answer_list[i-2] + answer_list[i-3]) 

for num in num_list:
    stdout.write(str(answer_list[num]) + "\n")