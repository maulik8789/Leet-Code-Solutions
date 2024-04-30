/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    let arr = [];
    for(let j = 0; j < numRows; j++){
        arr[j] = [];
    }
    let i = 0;
    let zig = false;
    let zigIdx;
    if(numRows == 1){
        return s;
    }
    for(let c = 0; c < s.length; c++){
        if(i < numRows){
            if(zigIdx == 1){
                zig = false;
            }
            if(zig){
                for(let j = 0; j < numRows; j++){
                  if(j == zigIdx - 1){
                    arr[j].push(s[c]);
                  }
                  else
                  {
                    arr[j].push("");
                   }
                }
                zigIdx--;
                i = 0;
                // if(zigIdx == 1){
                //     zig = false;
                //     continue;
                // }
            }
            if(!zig){
                arr[i].push(s[c]);
                i++;    
            }    
            
        }
        
        if(i == numRows){
            zig = true;
            zigIdx = i - 1;
            i = 0;
        }
                        
    }
    // console.log(arr);
    let ans = "";
    for(let j in arr){
        for(let k of arr[j]){
            ans += `${k}`;
        }
    }
    return ans;
};