from collections import deque


# bfs 이용
# 방문 처리 X (같은 수 여러 번 방문 가능하므로. ex) n = 3, '1 + 2' / '2 + 1')
def plus(n):
    q = deque([0])
    cnt = 0
    while q:
        curr = q.popleft()
        for i in range(1, 4):
            next_num = curr + i
            if next_num == n:
                cnt += 1
            elif next_num < n:
                q.append(next_num)
    return cnt


T = int(input())
for _ in range(T):
    n = int(input())
    print(plus(n))
