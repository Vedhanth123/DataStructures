class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if(a == b and b == c):

            return "equilateral"
        elif(a == b and b != c or b == c and b != a or a == c and a != b):

            if(a+b > c):
                if(a+c > b):
                    if(b+c > a):
                        return "isosceles"
        else:
            if(a+b > c):
                if(a+c > b):
                    if(b+c > a):
                        return "scalene"
        

        return "None"