'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''


class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        bIsValid = False
        
        for chr in s:
            if(chr == ')'):
                if(len(queue) > 0 and queue[-1] == '('):
                    bIsValid = True
                    queue.pop()
                else:
                    bIsValid = False
                    break
                
            elif(chr=='}'):
                if(len(queue) > 0 and queue[-1] == '{'):
                    bIsValid = True
                    queue.pop()
                else:
                    bIsValid = False
                    break
                
            elif(chr==']'):
                if(len(queue) > 0 and queue[-1] == '['):
                    bIsValid = True
                    queue.pop()
                else:
                    bIsValid = False
                    break
                
            else:
                queue.append(chr)

        if(len(queue) != 0):
            bIsValid = False
                
        return bIsValid

class BetterSolution:
    def isValid(self, s:str)->bool:
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack