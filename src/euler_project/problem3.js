/*
var input = 600851475143;
var primeFactors = [];

getPrimeFactors(input, primeFactors);
console.log(primeFactors);



function getPrimeFactors(input, primeFactors){
	var number = 1;
	do{
		number++;
		share = input / number;
	}while(input % number !==0);
	
	primeFactors.push(number);
	
	if(share !== 1)
		getPrimeFactors(share, primeFactors);
}*/

var number = 600851475143;
var maxPrime = 2;

while(maxPrime <= number){
	if(number % maxPrime === 0) {
		number = number / maxPrime;
	}
	else{ maxPrime++; }
}

console.log(maxPrime);