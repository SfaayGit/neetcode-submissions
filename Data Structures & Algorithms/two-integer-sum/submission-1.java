class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> twoSum = new HashMap<>();
        for(int i =0; i<nums.length; i++){
            int complement = target - nums[i];
           if(twoSum.containsKey(complement)){
        return new int[]{twoSum.get(complement), i};
            }
             twoSum.put(nums[i],i);
        }
        return new int[]{};
    }
}
