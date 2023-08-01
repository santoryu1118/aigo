"""
제목: 기타 레슨
숫자: 2343
유형: 이분 탐색
날짜: 2023-07-31
난이도: 4
메모: 생각보다 그냥 함수 짜는 것도 쉽지않네 ㅋㅋ
"""
import sys

sys.stdin = open('input.txt')

# N : 강의 개수, M : 블루레이 개수
N, M = list(map(int, sys.stdin.readline().split()))
duration_list = list(map(int, sys.stdin.readline().split()))


def is_possible(blueray_size):
    blueray_cnt = 0
    current_size = 0
    for duration in duration_list:
        if blueray_cnt > M:
            return False
        current_size += duration
        if current_size < blueray_size:
            continue
        elif current_size == blueray_size:
            blueray_cnt += 1
            current_size = 0
        else:
            blueray_cnt += 1
            current_size = duration
    if current_size > 0:
        blueray_cnt += 1
    # print("blueray_cnt", blueray_cnt)
    if blueray_cnt > M:
        return False
    return True


# 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.
min_size = max(duration_list)
max_size = sum(duration_list)

while min_size <= max_size:
    mid = (min_size + max_size) // 2
    # print('min_size:', min_size)
    # print('max_size:', max_size)
    # print('mid:', mid)
    if is_possible(mid):
        max_size = mid - 1
    else:
        min_size = mid + 1
    # print('----------------')

print(min_size)

