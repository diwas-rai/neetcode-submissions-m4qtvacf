class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r

        while l <= r:
            curr_speed = l + (r - l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / curr_speed)
            
            if time <= h:
                min_speed = curr_speed
                r = curr_speed - 1
            else:
                l = curr_speed + 1

        return min_speed