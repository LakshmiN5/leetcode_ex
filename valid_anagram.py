'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false'''

from collections import Counter

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        #return sorted(s)==sorted(t)
        c_first = Counter(s)
        c_second = Counter(t)
        print(f"c_first : {c_first}, c_second:{c_second} ")
        return c_first==c_second
    
solution_object = Solution()
#print(solution_object.strStr(haystack = "sadbutsad", needle = "sad"))
print(solution_object.isAnagram(s = "anagram", t = "nagaram"))