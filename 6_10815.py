"""
제목: 숫자 카드
숫자: 10815
유형: 이분 탐색
날짜: 2023-07-30
난이도: 4
메모:
"""

import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

ans = list(0 for i in range(len(checks)))

cards.sort()

# 시간 초과
# for i, m in enumerate(checks):
#     if m in cards:
#         ans[i] = 1
# print(ans)

# 이분 탐색
for i, check in enumerate(checks):
    low, high = 0, len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] == check:
            ans[i] = 1
            break
        elif cards[mid] < check:
            low = mid + 1
        elif cards[mid] > check:
            high = mid - 1

for i in ans:
    print(i, end=" ")

