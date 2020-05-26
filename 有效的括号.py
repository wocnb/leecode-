class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        
        
        sol = list()
        for i in s:
            n = len(sol)
            if len(sol) == 0:
                sol.append(i)
            else:
                #n = len(sol)
                if i == ')':
                    if sol[n-1] != '(':
                        return False
                    else:
                        sol.pop()
                elif i == ']':
                    if sol[n-1] != '[':
                        return False
                    else:
                        sol.pop()
                elif i == '}':
                    if sol[n-1] != '{':
                        return False
                    else:
                        sol.pop()
                else:
                    sol.append(i)
        
        if len(sol) == 0:
            return True
        else:
            return False
