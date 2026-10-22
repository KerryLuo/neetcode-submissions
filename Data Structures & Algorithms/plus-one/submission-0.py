class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1

        carry = 1

        while carry == 1:
            result = digits[index] + carry

            print(index, result)

            if result == 10:
                digits[index] = 0
                index -= 1

                if index == -1:
                    digits.insert(0, 1)
                    carry = 0
                print("updated index", index, "to", digits[index])
            else:
                digits[index] = result
                carry = 0
        
        return digits

