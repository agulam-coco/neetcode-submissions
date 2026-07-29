class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        hash_lookup = set(nums)
        max_seq = 0

        for num in nums:
            curr_seq = 1

            #s stat of sequence
            if num-1 not in hash_lookup:

                curr_num = num+1
                #find the rest
                while True:
                    if curr_num in hash_lookup:
                        curr_seq += 1
                    else:
                        break
                    
                    curr_num += 1
                max_seq = max(max_seq, curr_seq)

        return max_seq