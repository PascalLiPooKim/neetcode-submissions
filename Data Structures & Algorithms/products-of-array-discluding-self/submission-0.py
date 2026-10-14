class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # length = len(nums)
        # for i in range(length):
        #     product = 1
        #     for j in range(length):
        #         if j != i:
        #             product *= nums[j]
        #     result.append(product)

        # return result

        n = len(nums)
        result = [1] * n

        # Pass 1: result[i] = product of everything LEFT of i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Pass 2: multiply in the product of everything RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
            


