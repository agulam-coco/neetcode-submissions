
class Solution {
    public boolean hasDuplicate(int[] nums) {
 
        HashMap<Integer, Integer>  freqTable = new HashMap();

        //generate frequenccies
        for(int i = 0; i < nums.length; i++){
            //get or s4t and increment concise
            freqTable.put(nums[i], freqTable.getOrDefault(nums[i], 0) + 1);
            //increment by 1
            //freqTable.put(arr[i]. freqTable.get(arr[i])++);
        }

        for(int freq : freqTable.values()){
            if (freq > 1){
                return true;
            }
        }
        return false;
    }
}
