"""
제목: 최단경로
숫자: 1753
유형: BFS/DFS 가 아닌 Dijkstra 알고리즘
    Dijkstra 알고리즘 : 다이나믹 프로그래밍을 활용한 대표적인 최단 경로 탐색 알고리즘
    heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조
    heapq 에 튜플이 삽입될 경우엔, 튜플의 첫 번째 요소가 정렬의 기준.
날짜: 2023-08-23
난이도: 3
메모: Dijkstra 알고리즘과 heapq 처음 써봐서 좋았음
"""
import sys
from math import sqrt
from collections import deque
import heapq

sys.stdin = open('input.txt')
v, e = map(int, sys.stdin.readline().split())
start_node = int(sys.stdin.readline())

INF = int(1e9)

weighted_map = [[] for _ in range(v + 1)]
shortest_distance = [INF] * (v + 1)
shortest_distance[start_node] = 0

for _ in range(e):
    source, destination, weight = map(int, input().split())
    weighted_map[source].append((destination, weight))

print(weighted_map)

q = []
heapq.heappush(q, (0, start_node))
while q:
    distance, current_node = heapq.heappop(q)
    for dest, weight in weighted_map[current_node]:
        new_distance = distance + weight
        if new_distance < shortest_distance[dest]:
            shortest_distance[dest] = new_distance
            heapq.heappush(q, (new_distance, dest))

print(shortest_distance)

