class Solution(object):
    def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        # curr: 현재 만들고 있는 순열
        def dfs(curr, nums, result):
            # 모든 숫자를 사용해 순열을 만들었다면 종료
            if len(curr) == len(nums):
                result.append(curr.copy())
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs(curr, nums, result)
                    # 다음 숫자에 대해 같은 과정을 반복하기 위해 방금 추가한 num 제거
                    curr.pop()

        dfs([], nums, result)
        return result

    print(permute([1]))
