/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let m=nums.length;
    let arr=new Array(m+1).fill(-1);
    for (let i=0;i<nums.length;i++){
        arr[nums[i]]=nums[i];
    }
    console.log(arr);
    return (arr.findIndex(element => element == -1));
};