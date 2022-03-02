'''
    Explanation:
        - id passed in checkIn and checkOut: unique identifier to our customer
        - Each customer can only be checked into a station one place at a time
        
        1. Create a map called arrivals. key = id, value = tuple containing stationName and time --> (stationName, t)
        2. To keep track of all previous travels between any two stations, we create another map called travels. key = stationNames separated by a delimiter, value = count, total --> [count, total]
        
        Example:
        Calls                   Arrivals                Travels
        checkIn(1,A,3)          1 => (A,3)
        checkIn(2,A,10)         2 => (A,10)
        checkOut(1,B,5) --> look up the customer id in the arrivals map, remove the customer from arrivals map and compute the diff between start and end times
        checkOut(1,B,5)                                 A,B => (1,2)
        getAverageTime(A,B) --> combine the two stations and look it up in the travels map = 2 / 1 = 2.000000
        checkOut(2,B,20)                                A,B ==> (2,12)
        getAverageTime(A,B) --> 12 / 2 = 6
        
        
        
        TC - O(1) for all functions
        SC - O(n + m) where n is the number of arrivals and m is the number of travels. n grows larger when we have customers that check in but don't check out - we remove those entries from the arrivals map in the checkout function. m increases the more times the customers check out at various stations.
'''

class UndergroundSystem:
    def __init__(self):
        self.arrivals = dict()
        self.travels = dict()
        # {} --> O(n)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # if id in self.arrivals:
        #     raise Exception("customer already checked in")
        self.arrivals[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, start_time = self.arrivals[id]
        del self.arrivals[id]
        travel = station + "," + stationName
        if travel not in self.travels: self.travels[travel] = [0,0]
        trip = self.travels[travel]
        trip[0] += 1
        trip[1] += t - start_time # computing the  difference between start and end times
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, total = self.travels[startStation + "," + endStation]
        if count == 0 and total == 0:
            return "No customer has checked out at this moment"
        return total / count
    
    
    '''
    Example 1:
    
        Calls                   Arrivals                    Travels
        checkIn(45,L,3)         45 => (L,3)
        
        checkIn(32,P,8)         45 => (L,3)
                                32 => (P,8)
        
        checkIn(27,L,10)        45 => (L,3)
                                32 => (P,8)
                                27 => (L,10)
                                
        checkOut(45,W,15)       32 => (P,8)
                                27 => (L,10)                (L,W) => (1,12)
        
        checkOut(27,W,20)       32 => (P,8)                 (L,W) => (2, 22)
        
        checkOut(32,C,22)       empty                       (P,C) => (1, 14)
        
        getAverageTime()                                    (P,C) = 14/1 = 14
        
        getAverageTime()                                    (L,W) = 22/2 = 11
        
        checkIn(10,L,24)        10 => (L,24)
        
        getAverageTime()                                    (L,W) = 22/2 = 11
        
        checkout(10,W,38)       empty                       (L,W) => (3,36)
        
        getAverageTime()                                    (L,W) = 36/3 = 12
    '''