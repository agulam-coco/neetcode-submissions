class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search_rec(left:int , right: int) -> int:
            left_val = nums[left]
            right_val = nums[right]

            print("\nREC", left,right)
            # base cases
            if left == right:
                return left if nums[left] == target else -1

            elif left == right - 1:
                if left_val == target:
                    return left
                elif right_val == target:
                    return right
                else:
                    return -1
            #Recursive search case 
            else:
                mid = (left + right) // 2
                mid_val = nums[mid]

                print("MId", mid)

                if mid_val == target:
                    return mid
                
                elif (left_val <= mid_val):
                    if target > mid_val or target < left_val:
                        return search_rec(mid + 1, right)

                    else:
                        return search_rec(left, mid - 1)
                    
                else:
                    if target < mid_val or target > right_val:
                        return search_rec(left, mid -1)
                    else:
                        return search_rec(mid + 1, right)
                       




                    

        return search_rec(0,len(nums) -1)

         