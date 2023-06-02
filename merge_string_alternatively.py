'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''

class Solution:

    def mergeAlternately(self, word1:str, word2:str) -> str:
        # letters_in_word1 = word1.split(" ")
        # letters_in_word2 = word1.split(" ")
        # if len(letters_in_word1)>len(letters_in_word2):
        # print(word1)
        # zipped = zip(word1,word2)
        # print(zipped)
        concatenated = "".join([x+y for x,y in zip(word1,word2)])
        rem = abs(len(word2)-len(word1))
        residual = ""
        if len(word1)!=len(word2):
            residual = word1[-rem:] if len(word1)>len(word2) else word2[-rem:]
        return concatenated+residual



solution_object = Solution()
print(solution_object.mergeAlternately(word1 = "abc", word2 = "pqr"))

            
        

