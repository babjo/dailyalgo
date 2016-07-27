/**
 * @param {number} a
 * @param {number[]} b
 * @return {number}
 */

    var MOD = 1337;
    var superPow = function(a, b) {
        var result = 1;
        for(var i=b.length-1; i>=0; i--){
            result = powWithDiv(a%MOD, b[i]) * result % MOD;
            a = powWithDiv(a%MOD, 10);
        }
        return result;
    };

    function powWithDiv(a, pow){
        var result = 1;
        for(var i=0; i<pow; i++) result = result * a % MOD;
        return result;
    }

console.log(superPow(2, [3]));
console.log(superPow(2, [1, 0]));
console.log(superPow(2147483647, [2, 0 ,0]));
