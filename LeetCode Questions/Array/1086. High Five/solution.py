'''
    Explanation I: Dictionary & Sorting
        - Append the values from the items in the dictionary using ids as key and the scores as its values
        - Create a funtcion to calculate average. Function takes in a list as its parameter
            - Sort the list in an ascending order and then returns the integer for the division of the sum of the top 5 elements (average)
        - Now, create a res array and append the item for which we are calculating the average on the the id of the students
        - Return the Final array as sorted.
        
    - TC: O(nlogn), SC: O(n) for the nested output
    
    Explanation II: Max heap
    - Maintain a max heap of all the scores for every id
    - Top 5 scores ==> first 5 elements from the mex heap
    - Create an ordered map. key = student_id, value = scores. Scores for the same if are clubbed together in the same max heap
    - We are using an ordered map since we want the final scores to be in sorted order which can be obtained directly by iterating over the keys of the map
    - TC: 
        finding a key in the map - O(log n)
        pushing item into the max heap - O(log n)
        iterating over the map - O(n)
        extracting the top 5 elements - O(1)
        Overall = O(nlog n)
    - SC: O(n) used by hashmap map and max heap
'''


from typing import List

class Solution1:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = {}
        for item in items:
            if item[0] in dic:
                dic[item[0]].append(item[1])
            else:
                dic[item[0]] = [item[1]]
        
        def sort_avg(list):
            list  = sorted(list, reverse = True)
            return int((sum(list[0:5])/5))
        
        res = []
        for item in dic:
            res.append([item, sort_avg(dic[item])])

        return sorted(res)

from heapq import heappop, heappush, heapify

class Solution2:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        
        for item in items:
            studentId, score = item
            
            if studentId in hashmap:
                heap = hashmap[studentId]
                #print heap
                
                if len(heap) < 5:
                    heappush(heap, score)
                else:
                    if score > heap[0]:
                        heappop(heap)
                        heappush(heap, score)
            else:
                heap = [score]
                heapify(heap) # Heapifies the array in place
                
                hashmap[studentId] = heap
                #print hashmap[studentId]
        
        for item in hashmap.items():
            studentId, heap = item
            hashmap[studentId] = sum(list(heap)) // len(heap)
        
        return sorted(hashmap.items())