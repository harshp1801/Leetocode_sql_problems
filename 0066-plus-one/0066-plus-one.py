class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        out = []
        for i in digits:
            num = num*10+i
        for i in str(num+1):
            out.append(int(i))
        return out
