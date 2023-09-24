
nums = [1,2,2,3,3,4,5,5,6,7]

def removeDuplicates(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if i == j:
                nums.pop[i]
    return nums
print(removeDuplicates(nums))