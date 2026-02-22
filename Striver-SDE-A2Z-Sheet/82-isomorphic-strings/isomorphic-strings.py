class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False

        freq_s = {}
        freq_t = {}

        for x in range(len(s)):
            freq_s[s[x]] = freq_s.get(s[x], 0) + 1
            freq_t[t[x]] = freq_t.get(t[x], 0) + 1

        value_freq_t = {}
        for val in freq_t.values():
            value_freq_t[val] = value_freq_t.get(val, 0) + 1
        
        for val in freq_s.values():
            if(val not in value_freq_t):
                return False
            else:
                value_freq_t[val] -= 1
        
        return True



print(Solution().isIsomorphic(s = "egg", t = "add"))