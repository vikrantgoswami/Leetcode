class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #using one dictionary and one loop on strings
        #return if s & t are of different lengths

        if len(s) != len(t):
            return False

        char_count = {}

        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i],0) + 1 #increasing count for character at i in s
            char_count[t[i]] = char_count.get(t[i],0) - 1 #decreasing count for character at i in t
        #after above for loop if both s & t are anagrams then they will have same characters with same frequency
        #so increasing char count for s and decreasing char count for t for same character should give 0 for each letter
        #so if any of the value for any character is not 0 that means that character is occuring more times in any one of the string
        #thus these are not anagrams otherwise these are anagrams
        
        for value in char_count.values():
            if value != 0:
                return False
        
        return True