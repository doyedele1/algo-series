def getMinimumCost(parcels, k):

    parcel, toPick = set(parcels), 1
    remainingSum, remainingCount = 0, k - len(parcels)

    while remainingCount > 0:
        if toPick not in parcel:
            remainingSum += toPick
            remainingCount -= 1

        toPick += 1

    return remainingSum