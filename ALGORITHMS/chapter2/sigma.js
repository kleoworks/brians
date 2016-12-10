function sigma(num) {
    var sum = 0;
    for (var i = 1; i <= num; i++) {
        sum+=i;
    }
    return sum;
}

//test
console.log(sigma(3));
console.log(sigma(5));
