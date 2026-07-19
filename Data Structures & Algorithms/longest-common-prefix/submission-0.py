class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)
        result = ""

        for i, char in enumerate(shortest_word):
            for word in strs:
                if word[i] != char:
                    return result

            result += char

        return result
        