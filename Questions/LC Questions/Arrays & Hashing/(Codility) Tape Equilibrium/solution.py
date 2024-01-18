'''
    First iteration: 
        # first_sum = 3
        # second_sum = 10
        # diff = 13
        # new_diff = 3 - 10 = 7, which is less than diff. Then diff = 7

    Second iteration: 
        # first_sum = 4
        # second_sum = 9
        # diff = 7
        # new_diff = 4 - 9 = 5, which is less than diff. Then diff = 5

    Third iteration
        # first_sum = 6
        # second_sum = 7
        # diff = 5
        # new_diff = 6 - 7 = 1 which is less than diff. Then diff = 1

    Fourth iteration:
        # first_sum = 10
        # second_sum = 3
        # diff = 1
        # new_diff = 10 - 3 which is greater than diff. DO NOTHING!!!

    Fifth iteration:
        # first_sum = 13
        # second_sum = 0
        # diff = 1
        # new_diff = 13 - 0 = 13 which is greater than diff. DO NOTHING!!!

    TC: O(n-1), i.e. the number right before the end of the array, whose asymptotic notation is O(n) where n is the numbers on the tape
    SC: O(1) because we are not making use of extra space to store data in our computer memory
'''

def solution(arr):
    first_sum = 0
    second_sum = 0

    for i in range(len(arr)):
        second_sum += arr[i]
    
    diff = abs(first_sum - second_sum)

    for part in range(len(arr) - 1):
        first_sum += arr[part]
        second_sum -= arr[part]

        new_diff = abs(first_sum - second_sum)
        if new_diff < diff:
            diff = new_diff

    return diff

# print(solution([3,1,2,4,3]))