"""
제목: 최단경로
숫자: 1753
유형: BFS/DFS 가 아닌 Dijkstra 알고리즘
    Dijkstra 알고리즘 : 다이나믹 프로그래밍을 활용한 대표적인 최단 경로 탐색 알고리즘
날짜: 2023-08-06
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

# weighted_map = []
# # TODO: 이걸 어떻게 저장하는 것이 효율적인가
# for _ in range(e):
#     # 0 index : start_node, 1 index : destination_node, 2 index : weight
#     weighted_map.append(list(map(int, sys.stdin.readline().split())))
#
# print(weighted_map)
# visited = [-1] * (v + 1)
# visited[start_node] = 0
# print(visited)
#
# # 내 코드,....
# # de = deque([start_node])
# # while bool(de) is True:
# #     current_node = de.popleft()
# #     print("current_node", current_node)
# #     for node_line in weighted_map:
# #         if node_line[0] == current_node:
# #             destination_node = node_line[1]
# #             line_weight = node_line[2]
# #             if visited[destination_node] == -1:
# #                 visited[destination_node] = visited[current_node] + line_weight
# #                 de.append(destination_node)
# #             else:
# #                 if visited[destination_node] > visited[current_node] + line_weight:
# #                     visited[destination_node] = visited[current_node] + line_weight
# #                     de.append(destination_node)
#
# # chatgpt가 refactor한 내 코드;;;;; 분발하자
# de = deque([start_node])
# while de:
#     current_node = de.popleft()
#     print("current_node", current_node)
#     for source, destination, weight in weighted_map:
#         if source == current_node:
#             new_distance = visited[current_node] + weight
#             if visited[destination] == -1 or visited[destination] > new_distance:
#                 visited[destination] = new_distance
#                 de.append(destination)
#
# # 근데 시간초과 뜸...

weighted_map = [[] for _ in range(v + 1)]
for _ in range(e):
    source, destination, weight = map(int, input().split())
    weighted_map[source].append((destination, weight))

print(weighted_map)
INF = int(1e9)
distance = [INF] * (v + 1)
print(distance)


def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, current_node = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[current_node] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for destination, weight in weighted_map[current_node]:
            cost = dist + weight
            if cost < distance[destination]:
                distance[destination] = cost
                heapq.heappush(q, (cost, destination))


dijkstra(start_node)

for val in distance[1: v + 1]:
    print("INF" if val == INF else val)
