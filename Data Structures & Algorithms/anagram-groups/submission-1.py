class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Return single list if there is only one thing to return
        if len(strs) == 1:
            return [[strs[0]]]

        #Init lookup dict and count tracker
        lookup = dict()
        index = 0
        return_arr = []
        
        for string in strs:
            sort = str(sorted(string))

            # it is an anagram so insert at correct place 
            if  sort in lookup:
                return_arr[lookup.get(sort)].append(string)
            else:
                lookup[sort] = index
                return_arr.append([string])
                index += 1

        return return_arr