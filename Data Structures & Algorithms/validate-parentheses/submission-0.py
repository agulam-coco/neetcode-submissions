class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        lookup = {')':'(', '}' :'{', ']':'['}

        for char in s:

            #if opening char, add to stack
            if char in lookup.values():
                stack.append(char)
                #verify it is the right to be removed
            else:
                pair = lookup[char]
                if not len(stack) or stack[-1] != pair:
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True