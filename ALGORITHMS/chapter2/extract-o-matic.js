function extractDigit(num, digitNum) {

    if (digitNum == 0) {
        return num % 10;
    } else if (digitNum > 0) {
        //handle positive
        return (Math.floor(num / (Math.pow(10, digitNum))) % 10);
    } else {
        //handle negative
        return (Math.floor(num * (Math.pow(10,Math.abs(digitNum)))) % 10);
    }

}

//tests
console.log(extractDigit(1824,2));
console.log(extractDigit(1824,0));
console.log(extractDigit(1824,7));
console.log(extractDigit(123.45, -1));
console.log(extractDigit(123.45, -2));
console.log(extractDigit(123.456, -3));
