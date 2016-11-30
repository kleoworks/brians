function leapYear (a) {
    if (a % 400 === 0) {
        return true;
    } else if (a % 100 === 0) {
        return false;
    } else if (a % 4 === 0) {
        return true;
    } else {
        return false;
    }
}

// test, 30 leap years between 1900 and 2020
var count = 0;
for (var i = 1900; i <= 2020; i ++) {
    if (leapYear(i) === true) {
        console.log(i + " is a leap year.")
        count++;
    }
}
console.log(count);
