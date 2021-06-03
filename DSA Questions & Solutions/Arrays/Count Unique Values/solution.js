let countUniqueValues = function(nums) {
    let i = 0;
    
    if(nums.length === 0) {
        return 0;
    }

    for(let j = 1; j < nums.length; j++) {
        if(nums[i] !== nums[j]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}

console.log(countUniqueValues([1,1,1,1,1,2]));
console.log(countUniqueValues([1,2,3,4,5,5]));
//                                     i
//                                       j