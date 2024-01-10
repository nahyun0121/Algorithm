class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        arr = list(range(1, n + 1))

        if k == 0:
            return [[]]
        elif n < k:
            return [[]]

        # start: 다음에 탐색할 원소의 인덱스 / curr: 현재까지 선택한 원소들의 리스트
        def dfs(start, curr):
            # k개의 원소를 성공적으로 선택한 경우
            if len(curr) == k:
                result.append(curr.copy())
                return

            for i in range(start, n):
                curr.append(arr[i])
                # i + 1 이유: 같은 원소 중복 선택 방지
                dfs(i + 1, curr)
                # 백트래킹. 다른 조합을 찾기 위해 마지막 선택을 취소함
                curr.pop()

        dfs(0, [])
        return result


s = Solution()

result = s.combine(4, 2)
print(result)
