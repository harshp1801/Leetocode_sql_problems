class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        temp = x
        for i in range(len(str(x))):
            rem=x%10
            x = x//10
            num = num*10+rem
        if num - temp == 0:
            return True
        return False
 
        