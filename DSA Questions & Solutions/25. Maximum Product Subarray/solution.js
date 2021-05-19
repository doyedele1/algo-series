let maxProduct = function(nums) {
    // [2,3,-2,4]
    
    let maxOverallProd = maxAtEveryIndex = minAtEveryIndex = nums[0];
    
    for(let i = 1; i < nums.length; i++) {
        
        let temp = maxAtEveryIndex;
        
        maxAtEveryIndex = 
            Math.max(nums[i], Math.max(maxAtEveryIndex * nums[i], minAtEveryIndex * nums[i]));
        
        minAtEveryIndex = 
            Math.min(nums[i], Math.min(temp * nums[i], minAtEveryIndex * nums[i]));
        
        
        maxOverallProd = Math.max(maxOverallProd, maxAtEveryIndex);
    }
    
    return  maxOverallProd;
};

// console.log(maxProduct([2,3,-2,4]));
// console.log(maxProduct([-2,0,-1]));