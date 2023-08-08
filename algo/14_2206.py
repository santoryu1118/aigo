# """
# 제목: 벽 부수고 이동하기
# 숫자: 2206
# 유형: BFS/DFS
# 날짜: 2023-08-08
# 난이도: 4
# 메모:
# """
# import sys
# from collections import deque
#
# sys.stdin = open('input.txt')
# n, m = map(int, sys.stdin.readline().split())
# nmap = [[int(x) for x in line.strip()] for line in sys.stdin]
#
# # n, m = map(int, input().split())
# # nmap = [list(map(int, input())) for _ in range(n)]
#
# print(nmap)
#
# distance = [[(0, False)] * m for _ in range(n)]
# distance[0][0] = (1, False)
#
#
# def bfs():
#     moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     de = deque([(0, 0)])
#
#     while de:
#         x, y = de.popleft()
#         current_distance, is_broken = distance[y][x]
#
#         if x + 1 == m and y + 1 == n:
#             return current_distance
#
#         for move in moves:
#             new_x, new_y = x + move[0], y + move[1]
#             print('============')
#             print('x', x)
#             print('y', y)
#             print('new_x', new_x)
#             print('new_y', new_y)
#             print('current_distance', current_distance)
#
#             if 0 <= new_x < m and 0 <= new_y < n:
#                 print('nmap[new_y][new_x]', nmap[new_y][new_x])
#                 print('distance[new_y][new_x]', distance[new_y][new_x])
#                 if nmap[new_y][new_x] == 0 and distance[new_y][new_x][0] == 0:
#                     print('aa')
#                     distance[new_y][new_x] = (current_distance + 1, is_broken)
#                     de.append((new_x, new_y))
#
#                 elif nmap[new_y][new_x] == 1 and not is_broken:
#                     print('bb')
#                     distance[new_y][new_x] = (current_distance + 1, True)
#                     de.append((new_x, new_y))
#
#     return -1
#
# print(bfs())


import sys
from collections import deque

sys.stdin = open('input.txt')

# input = sys.stdin.readline
# n, m = map(int, input().split())
n, m = map(int, sys.stdin.readline().split())
print(n, m)
# graph = []
# for _ in range(n):
#     row = list(str(input().rstrip()))
#     graph.append(list(map(int, row)))
graph = [[int(x) for x in line.strip()] for line in sys.stdin]
print(graph)
# 3차원 배열 사용 -> visited[x][y][z], z = 0 or 1로 기록
# z = 0이면 벽을 뚫지 않고 간 경우, z = 1이면 벽을 뚫고 간 경우
moves = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()
        print(x, y, w)

        # 목표지점 도달 시 해당 위치까지의 거리 리턴
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for move in moves:
            nx, ny = x + move[0], y + move[1]

            if 0 <= nx < n and 0 <= ny < m:
                # 현재 위치로 이동할 수 있고, 아직 방문하지 않았다면
                if graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])

                # 현재 위치가 벽이고, 벽을 아직 부수지 않았다면
                elif graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append([nx, ny, w + 1])

    # 목표지점까지 도달하지 못한다면 -1 리턴
    return -1


print(bfs())