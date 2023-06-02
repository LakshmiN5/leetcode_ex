'''You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

 

Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
Example 2:

Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".'''

class Solution:
    def removeDigit(self, number:str, digit:str) -> str:
        number_new=[]
        counter = number.count(digit)
        print(counter)
        if counter>0:
            for i in range(len(number)):
                if int(number[i])==int(digit):
                    print(f"number[i] : {number[i]}")
                    number_new.append(number[:i]+number[i+1:])
                    print(number_new)
            return str(max(number_new))



solution_object = Solution()
print("#################3")
print(solution_object.removeDigit(number = "1243", digit = "4"))
