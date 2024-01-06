import heapq


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (heapq.nlargest(2, nums)[-1] - 1) * (heapq.nlargest(2, nums)[-2] - 1)


# heap.nlargest(n, iterable): iterable에 의해 정의된 데이터 집합에서 n개의 가장 큰 요소로 구성된 리스트 반환
