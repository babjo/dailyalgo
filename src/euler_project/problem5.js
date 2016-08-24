/*
var begin = 2;
var end = 20;
var result = 1;
var iter = 0;
for(var i=begin; i<=end; i++){
    if(result%i !== 0){
        for(var j=i-1; j>0; j--){
            iter++;
            if(i % j === 0)
                break;
        }
        if(j === 1){
            result *= i;
        }else{
            result *= j;
        }
    }
}
console.log(iter);
console.log(result);*/

var begin = 2;
var end = 20;
var result = 1;
var it = 0;
for(var i=begin; i<=end; i++){
    it ++;
    if(result%i !== 0){
        var gcd = getGcd(result, i);
        if(gcd === 1){
            result *= i;
        }else{
            result *= gcd;
        }
    }
}
console.log('반복수 : '+it);
console.log('답 : '+result);

function getGcd(a, b)
{
    var tmp;
    while(b) {
        it++;
        tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}
