"""
제목: 소수 경로
숫자: 1963
유형: BFS/DFS
날짜: 2023-08-03
난이도: 5
메모: 내 머리가 안좋은가.... 힌트를 안보면 아예 감이 안잡히네 어떻게 풀지
괜찮아 봐가면서 연습하면 되지~. 아 어제 에라토스테네스의 체 쓰는게 힌트구나 하하.....
답은 맞고 KeyError 뜨는데 모르겠다 헤헤
"""
import sys
from math import sqrt
from collections import deque


def get_prime_nums(n):
    is_prime = [False] * 2 + [True] * (n - 1)
    for num in range(2, int(sqrt(n) + 1)):
        i = 2
        while num * i <= n:
            is_prime[num * i] = False
            i += 1

    return [idx for idx, val in enumerate(is_prime) if val is True]


def bfs(a, b):
    prime_nums = get_prime_nums(b)
    between_prime_nums = [x for x in prime_nums if x >= a]
    # print(between_prime_nums)
    visited = dict((x, 10 ** 4) for x in between_prime_nums)
    visited[a] = 1

    de = deque([a])
    while bool(de) is True:
        current_num = de.popleft()
        # 4자리 숫자
        for digit_idx in range(4):
            for i in range(10):
                new_num_str = str(current_num)[:digit_idx] + str(i) + str(current_num)[digit_idx + 1:]
                new_num = int(new_num_str)
                if new_num in between_prime_nums:
                    if visited[new_num] > visited[current_num] + 1:
                        visited[new_num] = visited[current_num] + 1
                        de.append(new_num)

    if visited[b] == 10**4:
        print('Impossible')
    else:
        print(visited[b] - 1)


sys.stdin = open('input.txt')
t = int(sys.stdin.readline())
for _ in range(t):
    # 입력
    start, end = map(int, sys.stdin.readline().split())
    bfs(start, end)
