class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: filter to only alphanumeric chars, lowercased
        filtered = [c.lower() for c in s if c.isalnum()]

        # Step 2: two-pointer check
        left, right = 0, len(filtered) - 1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1

        return True