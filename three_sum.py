def threeSum(nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복 숫자 스킵
        if i > 0 and nums[i] == nums[i - 1]:  # 'i > 0'가 없으면 [0, 0, 0]과 같은 경우 for문 끝나버림
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                # 정답 찾은 후 중복 숫자 스킵
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


print(threeSum([1, -1, -1, 0]))
