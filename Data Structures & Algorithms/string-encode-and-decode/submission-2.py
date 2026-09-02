class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each string, start with a number as its length, followed by the encoded string, then the next number for the next word
        final = ""

        for item in strs:
            final += str(chr(len(item))) + item

        print(final)
        return final

    def decode(self, s: str) -> List[str]:

        # go by number, split the strings
        final = []
        
        code = list(s)

        pointer = 0

        for char in code:
            if pointer == 0:
                final.append("")
                pointer = int(ord(char))
            else:
                final[-1] += char
                pointer -= 1
        
        return final

        


