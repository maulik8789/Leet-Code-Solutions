/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for (i=0;i<=haystack.length-needle.length;i++){
        if (haystack.slice(i,i+needle.length)==needle){
            return i;
        }
    }
    return -1;
    
    
    
    //     Runtime: 60 ms
//     let isCounting=0;
//     let getNeedle='';
//     let firstOccur=-1;
//     let k=0
//     for (i=0;i<haystack.length;i++){
//         if (isCounting==0){
//             k=0;
//         }
//         for (j=k;j<needle.length;j++){
//             if(needle[j]==haystack[i]){
//                 if (j==0) {firstOccur=i;}
//                 isCounting=1;
//                 getNeedle+=needle[j];
//                 if(getNeedle==needle) {return firstOccur}
//                 k+=1;
//                 break
//             }
//             else{
//                 isCounting=0;
//                 if (getNeedle!=''){i=firstOccur;}
//                 getNeedle='';
                
//                 break;
//             }
//         }
//     }
//     return -1
};