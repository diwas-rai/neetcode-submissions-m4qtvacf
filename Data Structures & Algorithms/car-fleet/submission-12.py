class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p,s in zip(position, speed)]
        cars.sort(reverse=True)
        stk = []

        for p, s in cars:
            time_arrived = (target - p) / s
            stk.append(time_arrived)
            while len(stk) > 1 and stk[-2] >= stk[-1]:
                stk.pop()
                
        return len(stk)