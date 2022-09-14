'''
    Explanation I: Brute-force Solution
        - Convert the transactions to individual item of the valid data types and store it in an array. index.e. alice = string, 20 = integer, 800 = integer and mtv = string
        - Loop through the new array and find where amount > 1000. Append that to result array and convert the transaction to a string splitting each item by comma
            - Nested loop to check for same name, and if time difference is less than or equal to 60 and if different city,
                - Append that to the res array and convert the transaction to a string splitting each item by comma
        
        TC - O(n-squared)
        SC - O(n)xs

    Explanation II: Optimal Solution
        - Store all transactions done at a particular time in a dictionary. key = time, value = object --> key = person_name, value = location
        - ['alice,20,800,mtv', 'bob,50,1200,mtv', 'bob,20,100,beijing']
        - {   
            20: {'alice': {'mtv'}, 'bob': {'beijing'}}, 
            50: {'bob': {'mtv'}}
        }
        - Check if the amount is invalid, add it to the result
        - Go through the time (+-60), check if a transaction(the same person, a different city), add it to the result
        
        TC - O(n)
        SC - O(n)
'''

from collections import defaultdict
from typing import List

class Solution1:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []

        for i, trans1 in enumerate(transactions):
            name1, time1, amount1, city1 = trans1.split(',')
            if int(amount1) > 1000:
                res.append(trans1)
                continue

            for j, trans2 in enumerate(transactions):
                name2, time2, amount2, city2 = trans2.split(',')
                if name1 == name2 and abs(int(time1) - int(time2)) <= 60 and city1 != city2:                
                    res.append(trans1) # deals with duplicates by only appending t1
                    break
        return res

class Solution2:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []

        # Store all transactions done at a particular time in a dictionary
        transaction = defaultdict(dict)
        for trans in transactions:
            name, str_time, amount, city = trans.split(",")
            time = int(str_time)

            if name not in transaction[time]: transaction[time][name] = {city, }
            else: transaction[time][name].add(city)

        for trans in transactions:
            name, str_time, amount, city = trans.split(",")
            time = int(str_time)

            if int(amount) > 1000:
                res.append(trans)
                continue
            
            # Check within 60 minutes
            for invalid_time in range(time - 60, time + 61):
                if invalid_time not in transaction: continue
                if name not in transaction[invalid_time]: continue

                trans_city = transaction[invalid_time][name]

                # If transactions were done in a different city
                if city not in trans_city or len(trans_city) > 1:
                    res.append(trans)
                    break

        return res