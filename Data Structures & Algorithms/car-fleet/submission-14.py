class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort(reverse=True)
    
        stk = []
        for p, s in cars:
            time_arrived = (target - p) / s
            if stk and stk[-1] >= time_arrived:
                continue
            stk.append(time_arrived)
        
        return len(stk)