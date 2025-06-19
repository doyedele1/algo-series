// TC: O(nlogn), SC: O(1)
function partitionArray(nums: number[], k: number): number {
    const n = nums.length
    nums.sort((a, b) => a - b)

    let start_of_valid_subsequence = nums[0]
    let count = 1

    for (let i = 1; i < n; i++) {
        if (nums[i] - start_of_valid_subsequence > k) {
            start_of_valid_subsequence = nums[i]
            count++
        }
    }
    return count
};