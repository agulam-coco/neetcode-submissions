from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need_count = {}
        have_count = {}
        # calculate the need table
        for char in t:
            need_count[char] = 1 + need_count.get(char, 0)
        
        #reate he have and dneed counters
        have = 0
        need = len(need_count)

        l = 0
        res = [-1 , -1]
        resLen = inf

        #iterate every value
        for r in range(len(s)):
            c = s[r]
            have_count[c] = 1 + have_count.get(c, 0)

            #if this character is need and is the eexact number that we need, then added to have traacker
            if c in need_count and have_count[c] == need_count[c]:
                have += 1
            
            while have == need:
                current_window = r - l + 1
                if current_window < resLen:
                    resLen = current_window
                    res = [l,r]

                #keep removing from the left
                have_count[s[l]] -= 1

                #if have is not 
                if s[l] in need_count and have_count[s[l]] < need_count[s[l]] :
                    have -= 1
                
                l += 1

        l , r = res
        return "" if resLen == inf else s[l:r+1]



