import heapq

n, m = map(int, input().split())
cards = [*map(int, input().split())]
for _ in range(m):
    smallest = heapq.nsmallest(2, cards)[0]
    second = heapq.nsmallest(2, cards)[1]
    update = smallest + second
    cards[cards.index(smallest)] = update
    cards[cards.index(second)] = update

sum_list = sum(cards)
print(sum_list)
