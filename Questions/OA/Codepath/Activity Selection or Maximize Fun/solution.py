def activitySelection(activities, start, end):
    activities.sort()

    i = 0
    res = [activities[i]]

    for j in range(1, len(end)):
        if start[j] >= end[i]:
            res.append(activities[j])
            i = j

    return res

print(activitySelection(['a', 'b', 'c', 'd', 'e', 'f', 'g'], [0,1,5,6,8,10,11], [2,4,6,8,11,12,20]))