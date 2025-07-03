class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        if(nums.length < 2) {
            return false;
        }
        int slow = 0;
        int fast = 0;

        while(fast < nums.length) {
            slow = nums[slow];
            fast = nums[nums[fast]];

            if(slow == fast) {
                return true;
            }
        }

        return false;
        
    }
}