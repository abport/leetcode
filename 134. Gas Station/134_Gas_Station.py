class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total amount of gas is less than the total cost, it is not possible to complete the circuit
        if sum(gas) < sum(cost):
            return -1

        # Set the starting station to be the first station
        start = 0
        # Set the current amount of gas in our tank to be 0
        tank = 0
        # Iterate through each station
        for i in range(len(gas)):
            # Add the amount of gas we gain at this station to our tank, and subtract the cost of reaching the next station
            tank += gas[i] - cost[i]
            # If we run out of gas, set the starting station to be the next station and reset the tank
            if tank < 0:
                start = i + 1
                tank = 0
        # Return the starting station if we were able to complete the circuit, or -1 if not
        return start
