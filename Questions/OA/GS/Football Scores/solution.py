def counts(teamA, teamB):
    res = []
    teamA.sort()

    for score in teamB:
        low, high = 0, len(teamA) - 1
        while low <= high:
            mid = (low + high) // 2
            if teamA[mid] > score:
                high = mid - 1
            else:
                low = mid + 1
        res.append(low)

    return res