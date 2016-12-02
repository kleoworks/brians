function fTempToCelsius(fDegrees) {
    return (fDegrees - 32) / (9/5);
}

//tests
var test1 = fTempToCelsius(70);
var test2 = fTempToCelsius(90);
var test3 = fTempToCelsius(0);

console.log(test1);
console.log(test2);
console.log(test3);
