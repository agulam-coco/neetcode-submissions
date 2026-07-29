class Solution:
    def isPalindrome(self, s: str) -> bool:

        start_ptr = 0
        end_ptr = len(s) - 1

        while(start_ptr < end_ptr ):
            #skip all on alphanumeric character
            if not s[start_ptr].isalnum():
                start_ptr += 1
                continue

            if not s[end_ptr].isalnum():
                end_ptr -= 1
                continue
        
            if  s[start_ptr].lower() != s[end_ptr].lower():
                return False
            
            start_ptr += 1
            end_ptr -= 1
        
        return True