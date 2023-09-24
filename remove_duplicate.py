nums = [0,0,0,0,0,1,1,1,2,2,3,4,4,5,6,7,7]

def removeDuplicates(nums):
    unique = []
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            unique.append(nums[i])
    return unique
    
print(f' The Unique output is {removeDuplicates(nums)} ')