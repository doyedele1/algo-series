// Naive solution. TC - O(n-squared), SC - O(1)
function firstDuplicate(a) {
    for(let i = 0; i < a.length; i++) {
        for(let j = i+1; j < a.length; j++) {
            if(a[i] == a[j]) return a[i]
        }
    }
}

// TC - O(n), SC - O(n)
function firstDuplicate(a) {
    let seen = new Set([])
    for(let i = 0; i < a.length; i++) {
        if(seen.has(a[i])) {
            return a[i]
        }
        seen.add(a[i])
    }
    return -1
}

// TC - O(n), SC - O(1). Array mutated
function firstDuplicateOptimized(a) {
    for(let i = 0; i < a.length; i++) {
        if(a[Math.abs(a[i]) - 1] < 0) {
            return Math.abs(a[i])
        }
        else {
            a[Math.abs(a[i]) - 1] = -a[Math.abs(a[i]) - 1] 
        }
    }
    return -1
}

// TC - O(n), SC - O(1). Array not mutated
function firstDuplicateOptimizedAgain(a) {
    let slow = a[0]
    let fast = a[a[0]]

    slow = 1
    fast = 2

    while (fast != slow) {
        slow = a[slow]
        fast = a[a[fast]]
    }

    let slow = 0
    while (fast != slow) {
        slow = a[slow]
        fast = a[fast]
    }
    return slow
}

// console.log(firstDuplicate([1,2,1,2,3,3]))
// console.log(firstDuplicate([2,1,3,5,3,2]))
// console.log(firstDuplicate([1,2,3,4,5,6]))