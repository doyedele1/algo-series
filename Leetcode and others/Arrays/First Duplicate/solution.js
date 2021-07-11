function firstDuplicate(a) {
    let seen = new Set([])
    for(let i = 0; i < a.length; i++) {
        if(seen.has(a[i])) {
            return a[i]
        }
        seen.add(a[i])
    }
    return -1

    // Time complexity- O(n), Space complexity- O(n)
}

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

    // Time complexity- O(n), Space complexity- O(1)
}

console.log(firstDuplicate([1,2,1,2,3,3]))
console.log(firstDuplicate([2,1,3,5,3,2]))
console.log(firstDuplicate([1,2,3,4,5,6]))