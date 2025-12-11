class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        st = ''
        out = ""
        for i in strs:
            if len(i)<min_len:
                min_len = len(i)
                st = i
        for i in range(min_len):
            if i != len(st):
                for j in strs:
                    if j[i]!=st[i] or i>len(j):
                        return out
                out+=st[i]
        return out
