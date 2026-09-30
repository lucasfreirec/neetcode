class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = list(zip(position, speed))

        arr.sort(reverse=True)

        fleets = 0
        fleet_time = 0

        for p,s in arr:
            time = (target - p) / s

            if time > fleet_time:
                fleets += 1
                fleet_time = time
        
        return fleets