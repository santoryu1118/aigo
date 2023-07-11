"""
제목: 숫자의 합
숫자: 11720
유형:
날짜: 2023-07-11
난이도: 1
메모:
"""

N = int(input())
NUM_STR = str(input())

total = 0
for i in range(len(NUM_STR)):
    total += int(NUM_STR[i])

print(total)
