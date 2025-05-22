class Solution:
    def longestCommonPrefix(self, strs):
        
        # start from the first string
        answer = ""

        # first find the smallest string among the list of strings
        smallest = float("inf")
        smallest_string = ""
        for x in range(len(strs)):
            if(len(strs[x]) < smallest):
                smallest = len(strs[x])
                smallest_string = strs[x]
            

        for x in range(len(smallest_string)):

            answer += smallest_string[x]
            for y in range(len(strs)):

                if(answer and answer[-1] != strs[y][x]):
                    return answer[:-1]
        
        return answer

