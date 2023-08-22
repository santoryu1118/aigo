"""
제목: 최송 순위
숫자: 3665
유형: 위상 정렬
날짜: 2023-08-22
난이도: 4
메모: 이번엔 한번에 할 수 있을가
"""

import sys
from collections import deque

sys.stdin = open('input.txt')
t = int(sys.stdin.readline())


for i in range(t):
    n = int(sys.stdin.readline())

    indegree = [[] for _ in range(n + 1)]
    outdegree = [0] * (n + 1)
    old_ranking = list(map(int, sys.stdin.readline().rstrip().split()))
    new_ranking = []
    for idx, team in enumerate(old_ranking):
        indegree[team] = old_ranking[idx + 1:]
        for j in old_ranking[idx + 1:]:
            outdegree[j] += 1

    m = int(sys.stdin.readline())
    for _ in range(m):
        first, second = map(int, sys.stdin.readline().rstrip().split())
        outdegree[first] -= 1
        indegree[first].append(second)
        outdegree[second] += 1
        indegree[second].remove(first)

    que = deque()
    for idx, out_num in enumerate(outdegree):
        if idx > 0 and out_num == 0:
            que.append(idx)

    while que:
        current_team = que.popleft()
        new_ranking.append(current_team)
        for in_team in indegree[current_team]:
            outdegree[in_team] -= 1
            if outdegree[in_team] == 0:
                que.append(in_team)

    print(f"{new_ranking = }")
