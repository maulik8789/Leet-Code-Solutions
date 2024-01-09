/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // runtime 66ms
    let max = 0;
    let right = 1;
    let left = 0;
    // let profit = 0;
    while(right<prices.length){
        if(prices[right]>prices[left]){
            let profit = prices[right]-prices[left];
            max = Math.max(max,profit);
        }
        else{
            left = right
        }
        right++;
    }
    return max

    // Time Limit Exceeded: 199/212 testcases passed
    // let pr_s=0;
    // for (i=0;i<prices.length-1;i++){
    //         // console.log('i: ',i);
    //     for (j=i+1;j<prices.length;j++){
    //         // console.log('j: ',j);

    //         if (prices[j]-prices[i]>0 && prices[j]-prices[i]>pr_s){
    //             pr_s=prices[j]-prices[i];
    //         }
    //     }
    // }
    // return (pr_s)  


    // let pr_s=[0]
    // for (i=0;i<prices.length-1;i++){
    //         // console.log('i: ',i);
    //     for (j=i+1;j<prices.length;j++){
    //         // console.log('j: ',j);

    //         if (prices[i]-prices[j]<0){
    //             pr_s.push(prices[j]-prices[i]);
    //         }
    //     }
    // }
    // return Math.max(...pr_s)    
};