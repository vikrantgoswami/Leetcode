class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars   = set() #set of characters seen already in the string
        max_length   = 0     #length of longest substring without repeating chars
        l = 0
        n = len(s)
        for r in range(n):
            while s[r] in seen_chars:
                seen_chars.remove(s[l])
                l+=1
            seen_chars.add(s[r])
            max_length = max(max_length, r-l+1)

        return max_length
