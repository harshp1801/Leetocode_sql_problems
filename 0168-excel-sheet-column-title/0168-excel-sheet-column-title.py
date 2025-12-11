class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""
        while columnNumber > 0:
            columnNumber-=1
            out+=chr(columnNumber%26+ord('A'))
            columnNumber//=26
        return out[::-1]