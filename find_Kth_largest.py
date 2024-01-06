class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용함
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        # percolate: 스며들다. 새로 추가한 노드(current)의 인덱스는 len(self).
        current = len(self)
        # left, right, parent는 인덱스를 나타냄. left라면 2 * current, right라면 (2 * current + 1)
        parent = current // 2

        while parent > 0:
            if self.items[current] > self.items[parent]:
                self.items[current], self.items[parent] = (
                    self.items[parent],
                    self.items[current],
                )

            current = parent
            parent = current // 2

    def _percolate_down(self, current):
        biggest = current
        left = 2 * current
        right = 2 * current + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        # biggest가 바뀌었다면
        if biggest != current:
            self.items[current], self.items[biggest] = (
                self.items[biggest],
                self.items[current],
            )
            self._percolate_down(biggest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    maxheap = BinaryMaxHeap()

    for elem in nums:
        maxheap.insert(elem)

    return [maxheap.extract() for _ in range(k)][k - 1]


assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
