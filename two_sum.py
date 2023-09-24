# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.

nums = [4,3,6,8,4,1,7,9,3]
target = 6
def nums_check(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
answer = nums_check(nums, target)
print(answer)        
