/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let ans=0;
    for(i=0;i<nums.length-1;i++){
        for(j=i+1;j<nums.length;j++){
            if(nums[i]==nums[j]){
                ans+=1;
            }
        }
    }
    return ans;
};