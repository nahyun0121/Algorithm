def arrayPairSum(nums):
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
        sum += nums[i]
        print(sum)
    return sum


print(arrayPairSum([6, 2, 6, 5, 1, 2]))