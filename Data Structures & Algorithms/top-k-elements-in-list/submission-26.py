class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1

        max_heap = []

        for num, count in freqs.items():
            heapq.heappush(max_heap, [count, num])

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [num for count, num in max_heap]