# TC - O(nlogn), SC - O(1)
def solution1(arr, b):
    arr.sort()

    for num in arr:
        if num == b:
            b *= 2
    
    return b

def solution2(arr, b):
