let rotate = function(nums, k) {
    k = k % nums.length;
    
    reverseFn(nums, 0, nums.length-1);
    reverseFn(nums, 0, k-1);
    reverseFn(nums, k, nums.length-1);
}

let reverseFn = function(nums, start, end) {
    while (start < end) {
        let temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}

// console.log(rotate([1,2,3,4,5,6,7], 3));
// console.log(rotate([-1,-100,3,99], 2));
