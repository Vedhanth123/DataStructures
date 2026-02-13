class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        st1_freq = defaultdict(int)
        st2_freq = defaultdict(int)


        for x in range(len(s1)):

            st1_freq[s1[x]] += 1
            st2_freq[s2[x]] += 1
        
        if(st1_freq == st2_freq):

            different_st = 0
            for x in range(len(s1)):
                if(s1[x] != s2[x]):
                    different_st += 1
                    if(different_st > 2):
                        return False

            return True

        else:
            return False