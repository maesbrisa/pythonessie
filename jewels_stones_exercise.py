class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        chars_J = [b for b in J]
        chars_S = [b for b in S]
        counter = 0
        for char in chars_S:
            if char in chars_J:
                counter += 1
        return counter
