/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    var low = 1,
        high = num,
        mid = 0;

    while(low <= high){
        mid = Math.floor((low + high)/2);

        if(num == mid * mid){
            return true;
        }else if(num < mid * mid){
            high = mid-1;
        }else{
            low = mid+1;
        }
    }
    return false;
};

console.log(isPerfectSquare(16));