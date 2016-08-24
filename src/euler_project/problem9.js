// js a < b < c 이니 a 가 333 이상될 수 없음으로 아래와 같은 반복구조를 짰습니다.

/*
var a = 1;
var b;
var c;

do{
    b = a+1;
    do{
        c = 1000 - a - b;
        if( a*a + b*b === c*c) {
            console.log(a*b*c);
        }
        b++;
    }while(b<c);
    a++;
}while(a<333);*/

// 좀더 읽기 쉽게 바꾼 방법 -> for문으로 변경

console.log(primeNum(1000));

function primeNum(max){
    for(var a=1; a<max/3; a++){
        var c;
        for(var b=a+1; b<(c=max-a-b); b++){
            if( a*a + b*b === c*c) {
                return a*b*c;
            }
        }
    }
}