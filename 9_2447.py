# """
# 제목: 별 찍기 -10
# 숫자: 2447
# 유형: 분할 정복
# 날짜: 2023-08-01
# 난이도: 5
# 메모:
# """
import sys

N = int(input())
mapp = [["*" for _ in range(N)] for _ in range(N)]

def is_power_of(N, M):
    # Ensure both N and M are positive integers
    if N <= 0 or M <= 0:
        return False

    while N % M == 0:
        N //= M

    return N == 1


n = N
while n > 1:
    n = n // 3
    print("n", n)
    for y in range(1, N):
        for x in range(1, N):
            # if is_power_of(y - n, 3) and is_power_of(x - n, 3):
            if (y - n) % 3 == 0 and (x - n) % 3 == 0:
                for i in range(n):
                    print("y", y)
                    print("x", x)
                    print("n", n)
                    print("i", i)
                    print('x+n', x+n)
                    mapp[y+i][x: x+n] = " " * n

#
        n = 1 일때 x 1 4 7
        n = 3 일때 x 3 12 7
        for _i in mapp:
            for _j in _i:
                # print(mapp[i][j])
                print(_j, end="")
            print(end="\n")

        print('--------------------')