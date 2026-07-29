class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # HAve two pointers:
        #check if current substring is the same as the next adjacent substring, 
        #if not add one to count else shift current substring up by 1

        string_length = len(s)

        # quick end case
        if string_length == 0:
            return 0

        #INIT
        start_pointer = 0
        end_pointer = 0
        longest_substring = 0

        while end_pointer <=  string_length:
            # increment end
            end_pointer += 1

            curr_length = end_pointer - start_pointer

            current_set = set(s[start_pointer: end_pointer])

            # new longest without duplicate
            if curr_length == len(current_set):
                longest_substring = max(longest_substring + 1, curr_length)

            #move on not a substring
            else:
                #shift up by one
                start_pointer += 1

        return longest_substring




        