/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let arr=new Array(nums.length+1).fill(-1);
    for (let i=0;i<nums.length;i++){
        arr[nums[i]]=nums[i];
    }
    return (arr.findIndex(element => element == -1));
};