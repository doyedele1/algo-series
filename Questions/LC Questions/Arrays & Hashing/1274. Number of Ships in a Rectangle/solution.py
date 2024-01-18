'''
    TC: O(S(log2max(M,N)-log4S))
    SC: O(log2max(M,N))
'''

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:

class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def findShips(topRight, bottomLeft):
            # recursive base cases
            if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y: return 0
            elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))
            
            if not sea.hasShips(topRight, bottomLeft): return 0
            
            midX = (bottomLeft.x + topRight.x) // 2
            midY = (bottomLeft.y + topRight.y) // 2
            mid = Point(midX, midY)
            
            topLeftQuadrant = findShips(Point(midX, topRight.y), Point(bottomLeft.x, mid.y + 1))
            topRightQuadrant = findShips(topRight, Point(mid.x + 1, mid.y + 1))
            bottomRightQuadrant = findShips(Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))
            bottomLeftQuadrant = findShips(Point(mid.x, mid.y), bottomLeft)
            
            return topLeftQuadrant + topRightQuadrant + bottomRightQuadrant + bottomLeftQuadrant
        
        return findShips(topRight, bottomLeft)