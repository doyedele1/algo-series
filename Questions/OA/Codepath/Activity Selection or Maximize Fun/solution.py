def activitySelection(activities, start, end):
    i = 0
    res = [activities[i]]

    for j in range(1, len(end)):
        if start[j] >= end[i]:
            res.append(activities[j])
            i = j
    return res