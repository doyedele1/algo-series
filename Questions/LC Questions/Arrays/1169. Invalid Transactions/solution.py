'''
    Explanation I: Brute-force Solution
        - Loop through the array and find where amount > 1000. Append that to result array
            - Nested loop to check for same name, and if time difference is less than or equal to 60 and if different city,
                - Append that to the res array and convert the transaction to a string splitting each item by comma
        
        TC - O(n-squared)
        SC - O(n)

    Explanation II: Optimal Solution
        - Store all transactions done at a particular time in a dictionary. key = time, value = object --> key = name, value = city
        - ['alice,20,800,mtv', 'bob,50,1200,mtv', 'bob,20,100,beijing']
        { 
            20: {'alice': ['mtv'], 'bob': ['beijing']},
            50: {'bob': ['mtv']}
        }
        - Check if the amount is invalid, add it to the result
        - Go through the time (+-60), check a transaction (same name, different city), add it to the result
        
        TC - O(n)
        SC - O(1)
'''

from typing import List

class Solution1:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []

        for trans1 in transactions:
            name1, time1, amount1, city1 = trans1.split(',')
            if int(amount1) > 1000:
                res.append(trans1)
                continue # stop the current iteration and move to the next iteration

            for trans2 in transactions:
                name2, time2, amount2, city2 = trans2.split(',')
                if name1 == name2 and abs(int(time1) - int(time2)) <= 60 and city1 != city2:                
                    res.append(trans1)
                    break # breaks the loop completely
        return res

class Solution2:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        transactionMap = {}

        for trans in transactions:
            name, str_time, amount, city = trans.split(",")
            time = int(str_time)
            if time not in transactionMap:
                transactionMap[time] = {
                    name: [city]
                }
            else:
                if name not in transactionMap[time]:
                    transactionMap[time][name] = [city]
                else:
                    transactionMap[time][name].append(city)

        for trans in transactions:
            name, str_time, amount, city = trans.split(",")
            time = int(str_time)

            if int(amount) > 1000:
                res.append(trans)
                continue
            
            # Check within 60 minutes
            for invalid_time in range(time - 60, time + 61):
                if invalid_time not in transactionMap: 
                    continue
                if name not in transactionMap[invalid_time]: 
                    continue

                transaction_city = transactionMap[invalid_time][name]

                # If transactions were done in a different city
                if transaction_city[0] != city or len(transaction_city) > 1:
                    res.append(trans)
                    break

        return res

class Solution3:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        transactionMap = {}

        for trans in transactions:
            name, str_time, amount, city = trans.split(",")
            time = int(str_time)
            if time not in transactionMap:
                transactionMap[time] = {
                    name: {city}
                }
            else:
                if name not in transactionMap[time]:
                    transactionMap[time][name] = {city}
                else:
                    transactionMap[time][name].add(city)
        
        for trans in transactions:
            name, time, amount, city = trans.split(",")
            time = int(time)
            
            if int(amount) > 1000:
                res.append(trans)
            else:    
                for t in range(time-60, time):
                    if t in transactionMap and name in transactionMap[t]:
                        if len(transactionMap[t][name]) > 1 or city not in transactionMap[t][name]:
                            res.append(trans)
                            break
        return res