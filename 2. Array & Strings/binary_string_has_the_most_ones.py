class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        is_zero = False
        is_one = False
        for n in s:
            if n == '1' and is_zero == False:
                is_one = True
            elif n == '1' and is_zero == True:
                return False
            elif n == '0':
                is_zero = True
        
        return is_one
    
sol = Solution()
binary_string = "1001"
print(sol.checkOnesSegment(binary_string))