class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        
        nums = []

        for token in tokens:
            if token not in operators:
                nums.append(int(token))
            else:
                second, first = nums.pop(), nums.pop()
                
                if token == "+":
                    nums.append(first + second)
                elif token == "-":
                    nums.append(first - second)
                elif token == "*":
                    nums.append(first * second)
                else:
                    nums.append(int(first / second))
        print(nums)
        return int(nums[0])
                
