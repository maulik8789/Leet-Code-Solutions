/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let nums01 = Array.from(nums1);
    let len = nums01.length
     nums01=nums01.slice(0,(m));
    console.log(nums01);
    if (m==0){
        nums1.length=0;
        nums1.push(...nums2);
    }
    else if(n==0){

    }
    else{
        for(i=0;i<n;i++){
                //  console.log(nums2[i]);
            let isAdded=0;
            for(j=0;j<nums01.length;j++){

            if (nums2[i]<=nums01[j]){
                //  console.log(nums1[j]);
                nums01.splice(j,0,nums2[i]);
                isAdded=1;
                break;
            }
            }
            if(!isAdded){
                nums01.push(nums2[i]);
            }
        //  console.log(nums1);
        }
        console.log(nums01);
        nums1.length=0;
        nums1.push(...nums01);
    }
};