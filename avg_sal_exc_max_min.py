'''. Average Salary Excluding the Minimum and Maximum Salary
Easy
2K
174
Companies
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

'''

'''Approach
Here Firstly we find how many numbers are in between of the range [low,high][low, high][low,high].
Which we can simply find by doing high−low+1high - low + 1high−low+1
Now if we have these no. of number odd, then we need to check if our starting point (low)(low)(low) is oddoddodd or notnotnot.
If start is odd then answer will be (no. of number + 1) // 2.
else it will be no. of number // 2.'''


class Solution:

    def average(self, salary) -> float:
        salary=sorted(salary)
        return (sum(salary[1:len(salary)-1]))/(len(salary)-2 )

solution_object = Solution()
print(solution_object.average(salary = [4000,3000,1000,2000]))

