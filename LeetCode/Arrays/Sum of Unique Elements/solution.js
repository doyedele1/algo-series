let sumOfUnique = function(nums) {
    let freqCounter = {}
    let sum = 0
    
    for(let i = 0; i < nums.length; i++) {
        if(freqCounter[nums[i]] > 0) {
            freqCounter[nums[i]]++
        }
        else {
            freqCounter[nums[i]] = 1
        }
    }
    
    for(let key in freqCounter) {
        console.log(key)
        if(freqCounter[key] === 1) {
            sum = sum + Number(key)
        }
    }
    return sum
};

sumOfUnique([1,2,3,2]);