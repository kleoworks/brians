function factorial(num) {
    var j = 1;
    for (var i = 1; i <= num; i++) {
        j*=i;
    }
    return j;
}

//tests
console.log(factorial(3));
console.log(factorial(5));
