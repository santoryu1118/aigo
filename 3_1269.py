"""
제목: 대칭 차집합
숫자: 1269
유형: 정렬
날짜: 2023-07-12
난이도: 1 ~ 5
메모:
"""

A_count, B_count = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(len(A-B) + len(B-A))

# # 시간초과
# _A = []
# for i in A:
#     if i in B:
#         B.remove(i)
#     else:
#         _A.append(i)
#
# print(len(_A) + len(B))

