'''Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.'''

class Solution:
    def repeatedSubstringPattern(self, s:str) -> bool:
        n,t=len(s),''
        for i in range(n//2):
            t+=s[i]
            print(f"t:{t}, n:{n}, n//2 : {n//2}, i:{i}, n//(i+1):{n//(i+1)}, t*(n//(i+1)):{t*(n//(i+1))}")
            if t*(n//(i+1))==s: 
                print(n//(i+1))
                print(t*(n//(i+1)))
                return True
        return False
        
            

solution_object = Solution()
#print(solution_object.repeatedSubstringPattern(s = "abcabcabcabc"))            
print(solution_object.repeatedSubstringPattern(s = "abaababaab"))            