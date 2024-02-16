'''
    Explanation: 5 -> 7 -> 3 -> 8
        Brute force: 
            Merge 5 and 7
            5 -> 7

            Merge 3, 5 and 7
            3 -> 5 -> 7

            Merge 5, 7, 3 and 8. We have to iterate through the whole ll to find where to put 8 - not efficient. 
            TC: O(kn) - we have to iterate through every k list to merge
            3 -> 5 -> 7 -> 8

        Optimal:
            Merge 5 and 7
            5 -> 7

            Merge 3 and 8
            3 -> 8

            Merge 5 and 7 & 3 and 8
            3 -> 5 -> 7 -> 8


            TC: O(nlogk). Instead of iterating through k list, we only have to iterate log k times
            SC: O(1)
'''