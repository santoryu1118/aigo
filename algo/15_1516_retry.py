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

given_cost = [0] * (N + 1)
actual_cost = [0] * (N + 1)
depends_on = [[] for _ in range(N + 1)]  # idx가 필요해하는
depended_on = [[] for _ in range(N + 1)]  # idx의 후속으로 만들어지는
for idx in range(1, N + 1):
    line = list(map(int, sys.stdin.readline().split()))[:-1]
    given_cost[idx] = line[0]
    depends_on[idx] = line[1:]
    for pre_idx in line[1:]:
        depended_on[pre_idx].append(idx)

print(f'{N = }')
print(f'{given_cost = }')
print(f'{depends_on = }')
print(f'{depended_on = }')

q = deque()

for idx, idx_list in enumerate(depends_on):
    if idx > 0 and len(idx_list) == 0:
        q.append(idx)
print(q)

while q:
    current_idx = q.popleft()
    actual_cost[current_idx] += given_cost[current_idx]
    for depended_on_idx in depended_on[current_idx]:
        actual_cost[depended_on_idx] = max(actual_cost[current_idx], actual_cost[depended_on_idx])
        depends_on[depended_on_idx].remove(current_idx)
        if len(depends_on[depended_on_idx]) == 0:
            q.append(depended_on_idx)

print(f'{actual_cost = }')
