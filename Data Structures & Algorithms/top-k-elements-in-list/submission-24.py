class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        freqs = [(-count, num) for num, count in count.items()]
        heapq.heapify(freqs)

        res = []
        for i in range(k):
            res.append(heapq.heappop(freqs)[1])

        return res
