let containsDuplicate = function(nums) {
    let freqCounter = {}
    
    for(let i = 0; i < nums.length; i++) {
        if(freqCounter[nums[i]] > 0) {
            freqCounter[nums[i]]++
        }
        else {
            freqCounter[nums[i]] = 1
        }
    }
    
    for(num in freqCounter) {
        if(freqCounter[num] > 1) {
            return true
        }
    }
    return false
};