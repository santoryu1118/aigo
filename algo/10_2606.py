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


"""
스택(Stack): 가장 마지막에 삽입된 자료가 가장 먼저 삭제되는 구조 (LIFO)
큐(Queue): 먼저 들어온 것이 먼저 나가는 "선입선출" (FIFO)
"""
def bfs(idx):
    # queue를 써야겠지?
    from collections import deque
    de = deque([idx])
    while bool(de) is True:
        out_idx = de.popleft()
        visited[out_idx] = 1
        for adjacent_idx in graph[out_idx]:
            if visited[adjacent_idx] == 0:
                de.append(adjacent_idx)

    print(sum(visited) - 1)


bfs(1)
