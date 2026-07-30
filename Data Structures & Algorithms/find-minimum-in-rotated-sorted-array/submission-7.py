class Solution:
    def findMin(self, nums: List[int]) -> int:

        def search_rec(left, right, arr):
            #base case we found the smallest

            print("left is",left,"right is",right, "arr is",arr[left:right+1])
            if left == right:
                return arr[left]

            elif left == right - 1:
                return min(arr[left], arr[right])

            mid = (left + right) // 2

            right_val = arr[right]
            left_val = arr[left]
            mid_val = arr[mid]

            #search right half
            if right_val < left_val and right_val < mid_val:
                return search_rec(mid, right, arr)

            #search the left half
            else:
                return search_rec(left, mid, arr)
        
        return search_rec(0, len(nums) - 1, nums)