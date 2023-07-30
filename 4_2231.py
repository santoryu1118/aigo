"""
제목: 분해합
숫자: 2231
유형: 완전탐색
날짜: 2023-07-30
난이도: 1
메모:
"""

M = int(input()) #216 -> 198

for i in range(M+1):
    # num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    total = i + sum([int(x) for x in str(i)])
    if total == M:
        print(i)
        break
    elif i == M:
        print(0)
    else:
        continue


