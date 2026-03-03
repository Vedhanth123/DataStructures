class Solution:
    def myAtoi(self, s: str) -> int:

        MOD = 2**31

        def rec(s, index):

            # 4) Recurse till you find a non numeric character
            if index >= len(s) or not s[index].isnumeric():
                return (0, -1)

            prev_number, power = rec(s, index + 1)
            power += 1
            number = int(s[index]) * (10 ** (power)) + prev_number
            return (number, power)

        # 1) First strip the white spaces
        s = s.strip()
        if not s:
            return 0
        # 2) If the sign appears then put a -ve sign
        if s[0] == "-":
            answer = -1 * min(2**31, (rec(s, 1)[0]))
        # 3) If no sign appears then assume the number as the positive number
        elif s[0] == "+":
            answer = min((2**31) - 1, rec(s, 1)[0])
        else:
            answer = min((2**31) - 1, rec(s, 0)[0])

        return answer


Solution().myAtoi("-91283472332")
