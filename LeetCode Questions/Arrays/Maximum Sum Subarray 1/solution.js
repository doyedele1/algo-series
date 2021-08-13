let maxSubArray = function(nums) {
    // Naive solution
    // let maxSum = 0;

    // for(let i = 0; i < nums.length; i++) {
    //     let sum = 0;
    //     for(let j = i; j < nums.length; j++) {
    //         // console.log(nums[i],nums[j]);
    //         sum += nums[j];
    //         maxSum = Math.max(maxSum, sum);
    //     }
    // }
    // return maxSum;

    // Optimal solution - Kadane's algorithm
    let maxSum = maxAtEveryIndex = nums[0];
    
    for(let i = 1; i < nums.length; i++) {
        maxAtEveryIndex = Math.max(nums[i], maxAtEveryIndex + nums[i]);
        
        maxSum = Math.max(maxSum, maxAtEveryIndex);
    }

    return maxSum;
};

maxSubArray([-2,1,-3,4,-1,2,1,-5,4]);
maxSubArray([1]);
maxSubArray([5,4,-1,7,8]);