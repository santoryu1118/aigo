"""
제목: 바이러스
숫자: 2606
유형: BFS/DFS
날짜: 2023-08-02
난이도: 2
메모:
"""
import sys

n = int(input())  # 컴퓨터 개수
v = int(input())  # 연결선 개수

# sys.stdin = open('input.txt')
# n = int(sys.stdin.readline())
# v = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(v):  # 그래프 생성
    a, b = map(int, input().split())
    # a, b = list(map(int, sys.stdin.readline().split()))
    graph[b].append(a)
    graph[a].append(b)


def dfs(idx):
    visited[idx] = 1
    for connected_idx in graph[idx]:
        if visited[connected_idx] != 0:
            continue
        dfs(connected_idx)


dfs(1)
print(max(sum(visited) - 1, 0))
