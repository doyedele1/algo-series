'''
    Explanation: Use a bunch of data structures (deque, set)
        getCount: How does bisect work?

            Let's assume timestamps for destination 101 are [10, 20, 30, 40, 50]
            If we call getCount(101, 25, 45)
            
            bisect_left(timestamps, 25) -> 2 (index where 25 would go to keep timestamps sorted)
            bisect_right(timestamps, 45) -> 4 (index where 45 would go to keep timestamps sorted)
            Count = 4 - 2 = 2 (for timestamps 30 and 40)

        TC:
            addPacket: O(1) amortized
            forwardPacket: O(1) amortized
            getCount: O(K) where K is the number of packets for that specific destination

        SC: O(N) where N is the memoryLimit
'''
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packets_q = deque()
        self.unique_packets = set()
        # {destination: queue(timestamp)}
        self.dest_timestamps = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)   

        if packet in self.unique_packets:
            return False
        
        # memory full - remove the oldest packet
        if len(self.packets_q) == self.memoryLimit:
            oldest_packet = self.packets_q.popleft()
            self.unique_packets.remove(oldest_packet)

            old_dest = oldest_packet[1]
            self.dest_timestamps[old_dest].popleft()

        self.packets_q.append(packet)
        self.unique_packets.add(packet)
        self.dest_timestamps[destination].append(timestamp)
        
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets_q:
            return []

        oldest_packet = self.packets_q.popleft()

        self.unique_packets.remove(oldest_packet)
        old_dest = oldest_packet[1]
        self.dest_timestamps[old_dest].popleft()

        return list(oldest_packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_timestamps:
            return 0

        timestamps = self.dest_timestamps[destination]

        # use binary search to find the indices
        left_idx = bisect_left(timestamps, startTime)
        right_idx = bisect_right(timestamps, endTime)

        return right_idx - left_idx

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)