from collections import deque

N = int(input())
Dae_deq = deque(input() for _ in range(N))
Young_deq = deque(input() for _ in range(N))

count = 0
while 1:
    if Dae_deq == Young_deq:
        break
    if Dae_deq[0] != Young_deq[0]:
        Dae_deq.remove(Young_deq[0])
        Young_deq.popleft()
        count += 1
    else:
        Dae_deq.popleft()
        Young_deq.popleft()

print(count)

# ABCDE / BEDAC (B가 추월)
# ACDE / EDAC (E가 추월)
# ACD / DAC (D가 추월)
# AC / AC (같으므로 종료)
