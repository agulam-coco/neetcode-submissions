class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        freq_map = dict()

        #count up frequencies
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1


        #sort the frequencies and get the k largest frequencies
        return list(dict(sorted(freq_map.items(), key=lambda item: item[1], reverse=True)).keys())[0:k]