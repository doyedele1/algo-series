'''
    attendees = [1, 2, 3, 4]

    interests = {
        1: ['tech', 'health'],
        2: ['abc', 'def'],
        3: ['ai', 'ml']
    }

    sessions = {
        "session1": ['tech']
        "session2": ['health', 'abc']
        "session3": ['ml']
    }

    return [
    1: ["session1", "session2"],
    2: ["session1", "session2"]
    3: ["session3"]
    4: []
    ]

    TC: O(n * t) where n is the number of attendees, t is the number of topics
    SC: O(n)
'''

from typing import List

def solution1(attendees: List[int], interests, sessions):
    res = {}

    for attendee in attendees:
        attendeeSession = []

        if attendee in interests:
            for session, tags in sessions.items():
                for tag in tags:
                    if tag in interests[attendee]:
                        attendeeSession.append(session)
                        break

        res[attendee] = attendeeSession
    return res

def solution2(attendees: List[int], interests, sessions):
    res = {}

    for attendee in attendees:
        attendeeSession = []
        attendeeInterests = set(interests.get(attendee, []))

        for session, tags in sessions.items():
            if attendeeInterests.intersection(tags):
                attendeeSession.append(session)

        res[attendee] = attendeeSession
    return res

attendees = [1, 2, 3, 4]
interests = {
    1: ['tech', 'health'],
    2: ['abc', 'def'],
    3: ['ai', 'ml']
}
sessions = {
    "session1": ['tech'],
    "session2": ['health'],
    "session3": ['ml']
}

print(solution1(attendees, interests, sessions))
print(solution2(attendees, interests, sessions))