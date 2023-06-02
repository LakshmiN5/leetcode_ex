'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]'''

class Solution:
    def moveZeroes(self, nums) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     non_zero =zeros = []
    #     print(nums)
    #     non_zero = list([val for idx,val in enumerate(nums) if val!=0])
    #     zeros = list([val for idx,val in enumerate(nums) if val==0])
    #     print(f"non_zero:{non_zero} :  zeros:{zeros}")
    #     print(non_zero + zeros)
          i=0
          for j in range(len(nums)):
               print(f"i :{i}, nums[i] : {nums[i]}, j : {j},nums[j] : {nums[j]}")
               if nums[i]==0 and nums[j]!=0:
                   nums[i], nums[j] = nums[j] ,nums[i]
                   print("INSIDE IF 1")
                   print(f"i :{i}, nums[i] : {nums[i]}, j : {j},nums[j] : {nums[j]}")
               if  nums[i]!=0:
                    print("INSIDE IF 2")
                    i+=1
               print(nums)


solution_object = Solution()
#print(solution_object.moveZeroes(nums = [0,0,1]))            
print(solution_object.moveZeroes(nums = [0,1,0,3,12]))            