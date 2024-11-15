class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        n1 = len(t)
        n2 = len(s)
        t_char_count = {}
        for i in range(n1):
            t_char_count[t[i]] = t_char_count.get(t[i],0)+1
        #print('t_char_count ',t_char_count)
        req_chars = len(t_char_count)
        #print('req_chars ',req_chars)
        found_chars    = 0

        min_window_len = float(inf)
        ans = ""
        window = {}
        l = r = 0
        while r < n2:
            char = s[r]
            #we add character to our window
            window[char] = window.get(char,0)+1
            #print('window ',window)
            if char in t_char_count and window.get(char) == t_char_count.get(char,0):
                #if the character count is same, then we have found the reqd character
                found_chars += 1
                #print('Increasing found count ',found_chars)
            
            if found_chars == req_chars:
                #print('FC == RC')
                #if this is the case then we have found all characters in a particular substring
                #we can check if the length of the substring be minimised now while keeping the 
                #reqd characters count same
                while l <= r and found_chars == req_chars:
                    #print('min wind ',min_window_len)
                    #print('r ',r,' l ',l)
                    if min_window_len > r-l+1:
                        min_window_len = r-l+1
                        ans = s[l:r+1]
                    #print('ans ap is ',ans)
                    char_at_l = s[l]
                    l += 1
                    #now since we have moved past l, we need to decrease its count in our window
                    window[char_at_l] = window[char_at_l]-1
                    #print('removed ',char_at_l,' at ',l-1)
                    #print('window now is ', window)
                    if char_at_l in t_char_count and window[char_at_l] < t_char_count[char_at_l]:
                        #if we are here then we have move past the required character in the string
                        #so we have to decrease our count of found characters
                        found_chars -= 1
                        #print('decreasing fc to ',found_chars)
            r+=1

        return ans