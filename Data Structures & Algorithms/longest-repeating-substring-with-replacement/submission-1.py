class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l = 0
        longest_substring = 0
        max_frequency = 0

        # count of frequencies 
        for r in range(len(s)):
            #count while we iterate
            count[s[r]] = 1 + count.get(s[r], 0)
            max_frequency = max(count[s[r]], max_frequency)

            window_len = r - l + 1

            #if the window is invalid, remove from teh left to validate it 
            while window_len - max_frequency > k:
                #decrement from count dict
                count[s[l]] -= 1
                l += 1

                #recalc window - lenght
                window_len = r - l + 1

            longest_substring = max(longest_substring, window_len)
            
        return longest_substring
        