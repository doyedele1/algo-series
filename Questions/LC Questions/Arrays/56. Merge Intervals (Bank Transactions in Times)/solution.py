operatingTimes = ['04:20 - 12:30', '19:00 - 21:45', '14:00 - 17:30', '12:30 - 14:00']
transacTime = '04:00 - 17:30'

# Function to convert dates/times to minutes
def convertToMinutes(time):
    startMinutes = int(time[0 : 2]) * 60 + int(time[3 : 5])
    endMinutes = int(time[8 : 10]) * 60 + int(time[11 : 14])
    return startMinutes, endMinutes

bankStartMinutes = [None for x in range(len(operatingTimes))]
bankEndMinutes = [None for x in range(len(operatingTimes))]
#valid(bankStartMinutes, bankEndMinutes, operatingTimes, transacTime)

def valid(bankStartMinutes, bankEndMinutes, operatingTimes, transacTime):
    for idx in range(len(operatingTimes)):
        bankStartMinutes[idx], bankEndMinutes[idx] = convertToMinutes(operatingTimes[idx]) 
    validTranStart = min(bankStartMinutes)
    validTranEnd = max(bankEndMinutes)
    print(bankStartMinutes)
    print(bankEndMinutes)
    return validTransaction(validTranStart, validTranEnd, transacTime)
    
def validTransaction(validTranStart, validTranEnd, transacTime):
    startMinutes, endMinutes = convertToMinutes(transacTime)
    if startMinutes >= validTranStart and endMinutes <= validTranEnd:
        print(bool(True))
    else:
        print(bool(False))
valid(bankStartMinutes, bankEndMinutes, operatingTimes, transacTime)