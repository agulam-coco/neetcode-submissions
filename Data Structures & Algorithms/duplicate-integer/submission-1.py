class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #The idea is to check if each element is in a set, 
        #if it does not exist, add it to the set
        #else, it is a duplicate so return true
        #if no duplucates found, return alse
        
        lookup = set()

        for num in nums:
            if num in lookup:
                return True
            else:
                lookup.add(num)

        return False

        