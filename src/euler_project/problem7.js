// js

/*
var seq = 0;
var number = 1;

while(seq !== 10001){
    number++;
    if(isPrimeNumber(number)){
        seq++;
    }
}

console.log(number);

function isPrimeNumber(input){
    for(var i=2; i<input; i++){
        if( input % i === 0 && i < input) return false;
    }
    return true;
}*/

// js
// 3이상 홀수만 체크 -> 반복횟수 절반으로 줄음

var seq = 2;
var number = 3;
var it = 0;

while(seq !== 10001){
    number+=2;
    if(isPrimeNumber(number)){
        seq++;
    }
    it++;
}
console.log('반복문 횟수 : '+it);
console.log('답 : '+number);

function isPrimeNumber(input){
    for(var i=3; i<input; i++){
        if( input % i === 0 && i < input) return false;
    }
    return true;
}