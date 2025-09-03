class Solution(object):
    def isPalindrome(self, x):
        num = 0
        temp = x
        if temp<0:
            return False
        else:
            while temp>0:
                rem = temp%10
                num = num*10+(rem)
                temp = temp//10
        if num==x:
            return True
        else:
            return False

        