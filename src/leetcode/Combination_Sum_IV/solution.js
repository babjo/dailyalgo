//https://leetcode.com/problems/combination-sum-iv/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */


var combinationSum4 = function(nums, target) {
    var cache = {};
    for(var i=1; i<=target; i++){
        for(var j=0; j<nums.length; j++){
            if(!cache[i]) cache[i]=0;

            if(i == nums[j]) cache[i]++;
            else if(i > nums[j]) cache[i] += cache[i-nums[j]];
        }
    }
    return cache[target] ? cache[target] : 0;
};

console.log(combinationSum4([1, 2, 3], 32));
console.log(combinationSum4([1, 2], 3));
console.log(combinationSum4([], 1));
console.log(combinationSum4([3,33,333], 10000));
console.log(combinationSum4([1, 2, 3], 4));