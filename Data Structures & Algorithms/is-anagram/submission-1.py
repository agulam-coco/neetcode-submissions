class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_length = len(s)
        t_length = len(t)

        #if they are different lengths they cant be anagrams
        if(s_length != t_length):
            return False

        s_hash = dict()
        t_hash = dict()
        
        #count each cahr freq
        for i in range(0,s_length):
            s_hash[s[i]] = s_hash.get(s[i],0) + 1
            t_hash[t[i]] = t_hash.get(t[i],0) + 1

        #verify they are the same
        for key,val in s_hash.items():
            if key not in t_hash or val != t_hash[key]:
                return False
        return True


        