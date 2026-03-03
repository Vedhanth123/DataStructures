class Solution:
    def leaders(self, nums):

        # to find the leaders in an array we move from right to the left
        # we use a max value. it is the current leader
        # while iterating the nums array if the value is greater than the current leader then it is a leader and we update the leader and add that to the list of answers

        current_leader = float('-inf')
        answers = []

        for x in range(len(nums)-1,-1,-1):
            if(nums[x] > current_leader):
                current_leader = nums[x]
                answers.append(nums[x])
        
        return answers[::-1]
        
        ...

Solution().leaders([1,2,5,3,1,2])