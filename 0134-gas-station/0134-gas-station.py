class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        current_tank, starting_station, num_stations = 0, 0, len(gas)
        for station in range(num_stations):
            current_tank += gas[station] - cost[station]
            if current_tank < 0:
                starting_station = station + 1
                current_tank = 0 

        return starting_station