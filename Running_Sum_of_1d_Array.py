
def runningSum(nums):
    new = []
    running_sum = 0
    for i in nums:
        running_sum += i
        print(running_sum)
        new.append(running_sum)
    return new


    
nums = [1,2,3,4,5]
print(runningSum(nums))
