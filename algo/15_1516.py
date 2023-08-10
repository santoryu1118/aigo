"""
제목: 게임 개발
숫자: 1516
유형: 위상 정렬
날짜: 2023-08-10
난이도: 4
메모: 위상 정렬이 뭐지....
https://velog.io/@kimdukbae/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC-Topological-Sorting
정렬 알고리즘의 일종으로, 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다.
조금 더 이론적인 설명은, 사이클이 없는 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'을 의미한다.
"""

import sys
from collections import deque

sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

cost = [0] * (N + 1)
acc_cost = [0] * (N + 1)
indegree = [0] * (N + 1)
depending_from = [[] for _ in range(N + 1)]

for idx in range(1, N + 1):
    line = list(map(int, sys.stdin.readline().split()))[:-1]
    cost[idx] = line[0]
    for i in line[1:]:
        # indegree[idx].append(i)
        indegree[idx] += 1
        depending_from[i].append(idx)

print(f"{cost = }")
print(f"{acc_cost = }")
print(f"{indegree = }")
print(f"{depending_from = }")

q = deque()
for idx, dep_at in enumerate(indegree):
    if dep_at == 0:
        q.append(idx)

# depending_from = [[], [2, 3, 4], [], [4, 5], [], []]

while q:
    current_idx = q.popleft()
    acc_cost[current_idx] += cost[current_idx]
    for dep_from in depending_from[current_idx]:

        indegree[dep_from] -= 1
        print(f'{current_idx = }')
        print(f'{dep_from = }')
        print(f'{acc_cost[current_idx] = }')
        print(f'{acc_cost[dep_from] = }')
        acc_cost[dep_from] = max(acc_cost[dep_from], acc_cost[current_idx])
        print(f'{acc_cost[dep_from] = }')
        if indegree[dep_from] == 0:
            q.append(dep_from)


for i in range(1, N + 1):
    print(acc_cost[i])


