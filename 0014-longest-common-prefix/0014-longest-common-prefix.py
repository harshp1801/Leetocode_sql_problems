class Solution(object):
    def longestCommonPrefix(self, strs):
        m = len(strs[0])
        out = ''
        for i in range(m):
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!= strs[0][i]:
                    return out
            
            out+=strs[0][i]
        
        return out


            
        