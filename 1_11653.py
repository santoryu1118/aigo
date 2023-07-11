"""
제목: 소인수분해
숫자: 11653
유형:
날짜: 2023-07-10
난이도: 3
메모: 뭐여 오랜만에 알고리즘 문제 푸니까 이걸 못푸네....
"""

N = int(input())
result = []
div = 2
while N != 1:
    while N % div == 0:
        N = N / div
        result.append(div)
    div += 1

for i in result:
    print(i)
# return result
