import collections

class UndergroundSystem:
    
    def __init__(self):
        
        # customer_id: timestart and start_station
        self.check_in = collections.defaultdict(tuple)
        
        #start_station, end_station: time_end - time_start
        self.check_out = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (t, stationName)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, startStation = self.check_in[id]
        total = t - start_time
        self.check_out[(startStation, stationName)].append(total)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.check_out[(startStation, endStation)])/len(self.check_out[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


'''
    Explanation: Hint --> Use two hash tables. The first to save the check-in time for a customer and the second to update the total time between two stations
    
        1. Use a hash table to store the customer id inside of the check in and as well as the start time and the start station when we check out. Calculate the amount of time to get to the end station and put that in the hash table.
        
        Intuitive explanation:
            - Unique ids for all customers --> we need a hashmap
            
            checkIn(1, A, 3)        1 => (1, A, 3)      
            checkIn(2, A, 10)       2 => (2, A, 10)     
            checkOut(1, B, 5)
            getAverageTime(A, B)                        A, B => (2, 1)
            checkOut(2, B, 20)
            getAverageTime(A, B)                        A, B => (12, 2)
            
        TC - O(1) for checkIn, checkOut and getAverageTime
        SC - O(n + m) where n is the number of check_in and m is the number of check_out
        SC - O(P + S-squared) where S is the number of stations on the network and P is the number of passengers making a journey concurrently during peak time.
        checkIn = O(P)
        checkOut = O(S-squared) --> possible permutations between stations
        
        
        45: (3, Leyton)
        32: (8, Paradise)
        27: (10, Leyton)
        (Leyton, Waterloo): 12
        (Leyton, Waterloo): 10
        (Paradise, Cambridge): 14
        Average => 14/1 = 14
        Average => (10 + 12) / 2 = 11
        10: (24, Leyton)
        Average => Returns 11
        (Leyton, Waterloo): 14
        Average => (14 + 10 + 12) / 3 = 12
'''