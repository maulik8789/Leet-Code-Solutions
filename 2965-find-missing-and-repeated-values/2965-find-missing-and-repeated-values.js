/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    // Runtime: 117ms
    let o=[];
    let i;
    let grid1=[].concat(...grid);
    l=grid1.length;
    let ob={};
    for (i=0; i<grid1.length; i++){

        ob[grid1[i]] = isNaN(ob[grid1[i]]) ? 1 : (ob[grid1[i]] + 1);
        if(ob[grid1[i]]==2){
            o.unshift(grid1[i]);
        }
        if (!grid1.includes(i+1)){
            o.push(i+1);
        }
    }
    return o;
};