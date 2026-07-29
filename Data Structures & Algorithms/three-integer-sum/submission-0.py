class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        return_arr = []
        nums.sort()

        for i, num in enumerate(nums):
            #skip duplicate values on the left 
            if i > 0 and num == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1

            while l<r:
                curr_sum = nums[l] + nums[r] + num
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    return_arr.append([nums[l], nums[r], num])

                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return return_arr