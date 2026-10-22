class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(num):
            nums = [int(n) for n in list(str(num))]

            sum = 0

            for num in nums:
                sum += num * num
            
            return sum

        first = n
        second = n

        while True:
            first = sumSquares(first)
            second = sumSquares(sumSquares(second))

            if first == 1 or second == 1:
                return True
            elif first == second:
                return False
            

        
