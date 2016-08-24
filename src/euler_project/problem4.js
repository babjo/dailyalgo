/*
var number1 = 999;
var number2 = 999;

var palindromes = [];
for(var i=number1; i>=100; i--){
	for(var j=number2; j>=100; j--){
		if(number1 >= number2){
			var mul = i * j;
			if(isPalindrome(mul)){
				palindromes.push(mul);
			}
		}
	}
}

console.log(getMaxOfArray(palindromes));

function isPalindrome(number){
	var stringNum = String(number);
	var length = stringNum.length;
	for(var i=0; i<length/2; i++)
		if(stringNum[i] !== stringNum[length-1-i]) return false;
	
	return true;
}

function getMaxOfArray(numArray) {
    return Math.max.apply(null, numArray);
}
*/

var number1 = 999;
var number2 = 999;
var max = 0;

for(var i=number1; i>=100; i--){
	for(var j=number2; j>=100; j--){
		if(number1 >= number2){
			var mul = i * j;
			if(isPalindrome(mul) && max < mul) max = mul;
		}
	}
}

console.log(max);

function isPalindrome(number){
	var stringNum = String(number);
	var reverse = stringNum.split("").reverse().join("");
	return stringNum === reverse;
}