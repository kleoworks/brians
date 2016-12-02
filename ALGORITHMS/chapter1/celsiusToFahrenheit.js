function cTempToFahrenheit(cDegrees) {
    return (cDegrees * 9 / 5 + 32);
}

//tests
var test1 = cTempToFahrenheit(70);
var test2 = cTempToFahrenheit(90);
var test3 = cTempToFahrenheit(0);

console.log(test1);
console.log(test2);
console.log(test3);
