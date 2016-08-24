var length = 2000000;
var numbers = new Array(length);

for(var i=0; i<numbers.length; i++)
    numbers[i] = true;

var sum = 0;

var primeNum = 1;
while( ( primeNum = getNaxtPrimeNum(numbers, primeNum) ) !== -1){
    sum += primeNum;
    for(var n = primeNum; n <= numbers.length; n += primeNum){
        if(n !== primeNum){
            numbers[n-1] = false;
        }
    }
}

function getNaxtPrimeNum(numbers, index){
    for(var i=index; i<numbers.length; i++){
        if(numbers[i]) return i+1;
    }
    return -1;
}

console.log(sum);
