function isPrime(num) {
    for (var i = 2; i <= Math.floor(Math.sqrt(num)); i+=1) {
        if (num % i == 0) {
            return num + " is NOT prime";
        }
    }
    return num + " is prime!";
}

//test

console.log(isPrime(25));
console.log(isPrime(103));
console.log(isPrime(107));
console.log(isPrime(263));
console.log(isPrime(1200));
