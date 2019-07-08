def var(nums):
    m = (sum(nums)/len(nums))
    v = 0
    for i in nums:
        v += (m - nums[i]) ** 2
    return v/ len(nums)

nums=[1,5,1,2,1]
print(var(nums))
