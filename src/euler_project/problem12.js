var triangularNumbers = 1;
var nextNumber = 2;

var start = now();
while(countDivisor(triangularNumbers) < 500){
    triangularNumbers += nextNumber;
    nextNumber++;
}
var end = now();

console.log(triangularNumbers);
console.log((end-start)/1000);

/*
function countDivisor(number){
    if(number === 1) return 1;

    var count = 2; // 1과 자기자신은 약수로 가지고 시작한다.
    var share = number;

    for(var i = 2; i < share; i++){
        if(number % i === 0){
            share = number / i;
            share === i ? count ++ : count += 2;
        }
    }
    return count;
}*/

function countDivisor(number){
    var primeNum = 2;
    var exponential = 0;
    var count = 1;

    while(primeNum <= number){
        if(number % primeNum === 0) {
            number = number / primeNum;
            exponential ++;
        }
        else{
            primeNum++;
            count = count * (exponential + 1);
            exponential = 0;
        }
    }

    return  count * (exponential + 1);
}



function now(){
    var today = new Date() // 현재시간 얻기
    var RunTime = today.getTime(); // 밀리초 from 1/1/70
    return RunTime;
}