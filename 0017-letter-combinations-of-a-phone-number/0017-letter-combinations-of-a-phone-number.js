/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits==''){
        return [];
    }
    
    let o={
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
        '0':[' ']
    };
    if (digits.length==1){
        return o[digits];
    }
    // let ans=[];
    // console.log(o[digits[0]]);
    let ans=[];
    let str='';
    function backtrck(combination, nextDigit){
        if (!nextDigit){
            ans.push(combination);
            return;
        }
        
        for (let ltr of o[nextDigit[0]]){
            let newCom=combination+ltr;
            backtrck(newCom,nextDigit.slice(1));
        }
    }
    backtrck("", digits)
    return ans;
};