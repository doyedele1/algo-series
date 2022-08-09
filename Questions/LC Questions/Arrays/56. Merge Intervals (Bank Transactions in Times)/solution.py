# First Solution - Sorting. TC: O(nlogn), SC: O(1)
def solution(operatingHours, transaction):
    operatingHours.sort(key= lambda i: i[0])
    start, end = float("-inf"), float("-inf")

    for i in range(len(operatingHours)):
        if operatingHours[i][0] <= end:
            end = max(end, operatingHours[i][1])
        else: 
            start = operatingHours[i][0]
            end = operatingHours[i][1]
        
        if transaction[0] >= start and transaction[1] <= end: return True
    return False
print(solution([[600, 660], [720, 780]], [600, 780]))



# Doesn't work for some test cases --> Second Solution - Without Sorting. TC: O(n), SC: O(n)
operatingHours = ['10:00 - 11:00', '12:00 - 13:00']
transaction = '10:00 - 13:00'

# Function to convert dates/times to minutes
def convertToMinutes(time):
    start = int(time[0 : 2]) * 60 + int(time[3 : 5])
    end = int(time[8 : 10]) * 60 + int(time[11 : 14])
    return start, end

bankTransactionStartArr = [None for i in range(len(operatingHours))]
bankTransactionEndArr = [None for i in range(len(operatingHours))]

def solution(bankTransactionStartArr, bankTransactionEndArr, operatingHours, transaction):
    for i in range(len(operatingHours)):
        bankTransactionStartArr[i], bankTransactionEndArr[i] = convertToMinutes(operatingHours[i])

    print(bankTransactionStartArr)
    print(bankTransactionEndArr)
    validTranStart = min(bankTransactionStartArr)
    validTranEnd = max(bankTransactionEndArr)
    return checkIfInIntervals(validTranStart, validTranEnd, transaction)
    
def checkIfInIntervals(validTranStart, validTranEnd, transaction):
    startTransactionMinutes, endTransactionMinutes = convertToMinutes(transaction)
    if startTransactionMinutes >= validTranStart and endTransactionMinutes <= validTranEnd: return True
    else: return False
print(solution(bankTransactionStartArr, bankTransactionEndArr, operatingHours, transaction))