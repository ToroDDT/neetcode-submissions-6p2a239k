# need to check the last value in the stack 
# Because I can only remove it from the end if their is a match and 
# I can only remove from the end in any case

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingBrackets = {"}": "{", ")":"(", "]": "["}
        for c in s:
            if c in matchingBrackets:
                if stack and stack[-1] == matchingBrackets[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            

            
