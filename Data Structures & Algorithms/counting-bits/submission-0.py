class Solution:
    def countBits(self, n: int) -> List[int]:
        return [n.bit_count() for n in range(n + 1)]