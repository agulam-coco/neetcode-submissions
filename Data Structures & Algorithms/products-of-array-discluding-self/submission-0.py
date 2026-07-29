class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Build two arrays
        # One for calculating the left prefixes of all multipliction
        # One for calculating the right prefixes of all multiplications
        # We multiply both indexes together to get the result

        left = right = 1
        left_array = []
        right_array = []
        return_array = []
        array_length = len(nums)

        #fill in right array
        for i in range(array_length - 1, -1, -1):   
            right_array.insert(0, right)
            right *= nums[i]

        #fill in left array
        for i in range(array_length):   
            left_array.append(left)
            left *= nums[i]  

        #fill in return array 
        for i in range(array_length):
            return_array.append(left_array[i] * right_array[i])

        return return_array