from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        
        nums = deque()

        def operation(operator):
            second = nums.pop()
            first = nums.pop()
            
            if operator == "+":
                nums.append(int(first) + int(second))
            elif operator == "-":
                nums.append(int(first) - int(second))
            elif operator == "*":
                nums.append(int(first) * int(second))
            else:
                nums.append(int(first) / int(second))

        for token in tokens:
            if token not in operators:
                nums.append(token)
            else:
                operation(token)
        
        return int(nums[0])
                
