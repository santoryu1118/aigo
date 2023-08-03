"""
제목: 에디터
숫자: 1406
유형: 정렬
날짜: 2023-07-11
난이도: 1 ~ 5
메모:
"""
from sys import stdin

input_word = list(input())
cnt = int(input())

idx = len(input_word)

for _ in range(cnt):
    command = list(stdin.readline().split())
    cmd = command[0]
    if cmd == 'L':
        if idx == 0:
            continue
        else:
            idx -= 1
    elif cmd == 'D':
        if idx == len(input_word):
            continue
        else:
            idx += 1
    elif cmd == 'B':
        if idx == 0:
            continue
        else:
            # del input_word[idx - 1]
            input_word.pop(idx - 1)
            idx -= 1

    elif cmd == 'P':
        input_word.insert(idx, command[1])
        idx += 1

print(''.join(string_list))