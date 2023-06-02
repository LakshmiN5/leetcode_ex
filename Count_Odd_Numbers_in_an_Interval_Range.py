'''Approach
Here Firstly we find how many numbers are in between of the range [low,high][low, high][low,high].
Which we can simply find by doing high−low+1high - low + 1high−low+1
Now if we have these no. of number odd, then we need to check if our starting point (low)(low)(low) is oddoddodd or notnotnot.
If start is odd then answer will be (no. of number + 1) // 2.
else it will be no. of number // 2.'''


class Solution:
    # def countOdds(self, low:int, high:int) -> int:
    #     count=0
    #     for i in range(low,high+1):
    #         if i%2!=0:
    #             count+=1              
    #     return count

    def countOdds(self, low:int, high:int) -> int:
        count_of_numbers_in_range = high-low + 1 
        if low%2!=0:
            return (count_of_numbers_in_range+1)//2
        else:
            return (count_of_numbers_in_range//2)

solution_object = Solution()
print(solution_object.countOdds(3,10))

