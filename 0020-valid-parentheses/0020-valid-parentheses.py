class Solution(object):
    def isValid(self, s):
        stck = []
        ch = ''
        for i in s:
            if i in '({[':
                stck.append(i)
            elif i in ')]}':
                if len(stck)==0:
                    return False
                else:
                    ch=stck.pop()
                    if ch=='(' and i==')' or ch=='[' and i==']' or ch=='{' and i=='}':
                        continue
                    else:
                        return False
        if len(stck)>0:
            return False
        else:
            return True
                    
        