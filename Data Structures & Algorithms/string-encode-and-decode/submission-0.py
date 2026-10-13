class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # read digits up to '#' to get the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # the string starts right after '#'
            start = j + 1
            result.append(s[start:start + length])

            # jump past this string to the next length prefix
            i = start + length
        return result