class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            # 새로운 부분 집합: 현재까지 만들어진 모든 부분 집합 + 현재 숫자
            new_subsets = [curr + [num] for curr in result]
            # 새로운 부분 집합을 result에 추가함
            result.extend(new_subsets)
        return result


s = Solution()

print(s.subsets([1, 2, 3]))
