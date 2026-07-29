class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        freq_map = dict()

        #count up frequencies
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # place into buckets
        buckets = [[] for i in range(len(nums)+1)]

        for num, frequency in freq_map.items():
            buckets[frequency].append(num)

        #now read off in decending order the largest frequencies
        return_arr = []
        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                return_arr.append(num)
                if len(return_arr) == k:
                    return return_arr
