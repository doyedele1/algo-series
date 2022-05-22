function maxSubarraySum(arr, n) {

    if (arr.length < n) return null;

    let total = 0;
    for (let i=0; i<n; i++){
        total += arr[i];
    }

    let currentTotal = total;
    for (let i = n; i < arr.length; i++) {
        currentTotal += arr[i] - arr[i-n];
        total = Math.max(total, currentTotal);
    }
    
    return total;
}



// console.log(maxSubarraySum([1,2,5,2,8,1,5],2)) // 10
// console.log(maxSubarraySum([1,2,5,2,8,1,5],4)) // 17
// console.log(maxSubarraySum([4,2,1,6],1)) // 6
// console.log(maxSubarraySum([4,2,1,6,2],4)) // 13
// console.log(maxSubarraySum([],4)) // null