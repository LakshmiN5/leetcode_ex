
'''Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
'''

import time
def pivotIndex(nums):
    left_sum = 0
    right_sum = 0
    for idx, x in enumerate(nums):
        print(*nums, sep=',')
        end = len(nums)
        left_sum = 0 if idx==0 else sum(nums[:idx])
        right_sum = 0 if idx==end else sum(nums[idx+1:end])
        #right_sum = sum(nums[idx+1:len(nums)-1])
        print(f"left_sum : {left_sum}, right_sum : {right_sum}")
        if left_sum==right_sum:
            return idx
            
    
    return -1
  



    

start = time.time()
#nums = [2,1,-1]
nums = [1,7,3,6,5,6]
#nums = [1,2,3]
print(pivotIndex(nums))
end = time.time()
print(f"Code execution time : {(end-start)*1000}ms")
