import sys
from collections import deque

sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

given_cost = [0] * (N + 1)
actual_cost = [0] * (N + 1)
depends_on = [[] for _ in range(N + 1)]  # idx가 필요해하는
depended_on = [[] for _ in range(N + 1)]  # idx의 후속으로 만들어지는
for idx in range(1, N + 1):
    line = list(map(int, sys.stdin.readline().split()))[:-1]
    given_cost[idx] = line[0]
    depends_on[idx] = line[1:]
    for pre_idx in line[1:]:
        depended_on[pre_idx].append(idx)

print(f'{N = }')
print(f'{given_cost = }')
print(f'{depends_on = }')
print(f'{depended_on = }')

q = deque()

for idx, idx_list in enumerate(depends_on):
    if idx > 0 and len(idx_list) == 0:
        q.append(idx)
print(q)

while q:
    current_idx = q.popleft()
    actual_cost[current_idx] += given_cost[current_idx]
    for depended_on_idx in depended_on[current_idx]:
        actual_cost[depended_on_idx] = max(actual_cost[current_idx], actual_cost[depended_on_idx])
        depends_on[depended_on_idx].remove(current_idx)
        if len(depends_on[depended_on_idx]) == 0:
            q.append(depended_on_idx)

print(f'{actual_cost = }')
