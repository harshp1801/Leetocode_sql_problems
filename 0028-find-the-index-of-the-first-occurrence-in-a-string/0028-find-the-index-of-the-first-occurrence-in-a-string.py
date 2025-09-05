class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(0,len(haystack)):
            st = haystack[i:n+i]
            if needle==st:
                return i
        return -1
