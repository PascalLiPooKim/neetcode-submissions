class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: bucket by frequency (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 3: walk buckets from highest frequency down
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

