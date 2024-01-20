/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let isCounting=0;
    let getNeedle='';
    let firstOccur=-1;
    let k=0
    for (i=0;i<haystack.length;i++){
        if (isCounting==0){
            k=0;
        }
        console.log('i:k',i,k)
        for (j=k;j<needle.length;j++){
            console.log(needle[j],haystack[i])
            if(needle[j]==haystack[i]){
                if (j==0) {firstOccur=i;}
                isCounting=1;
                getNeedle+=needle[j];
                console.log(getNeedle);
                console.log('firtoccur',firstOccur);
                if(getNeedle==needle) {return firstOccur}
                k+=1;
                break
            }
            else{
                isCounting=0;
                if (getNeedle!=''){i=firstOccur;}
                getNeedle='';
                
                break;
            }
        }
    }
    return -1
};