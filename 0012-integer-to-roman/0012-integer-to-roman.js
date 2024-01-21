/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let o={
        'I':1,
        'IV':4,
        'V':5,
        'IX':9,
        'X':10,
        'XL':40,
        'L':50,
        'XC':90,
        'C':100,
        'CD':400,
        'D':500,
        'CM':900,
        'M':1000
    }
    
    let ans='';
    let k=Object.keys(o);
    while(num>0){
        for (let i=0; i<k.length;i++){
            if(o[k[i]]>num){
                ans+=k[i-1];
                num=num-o[k[i-1]];
                break;
                if (num==0){
                    break;
                }
            }
            else if(o[k[k.length-1]]<=num){
                ans+=k[k.length-1];
                num=num-o[k[k.length-1]];
                break;
            }
        }    
    }
    return ans;
};