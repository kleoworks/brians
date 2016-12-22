function mostSignificantDigit(num) {

    if (num >= 1) {

        while(true) {

            // check if loop has found the most significant bit
            if ((num / 10) <= 1) {
                return num % 10;
            }

            num = Math.trunc(num / 10);
        }


    } else {

        while(true) {

            if (num * 10 >= 1) {
                return Math.trunc(num * 10);
            }

            num = num * 10;

        }

    }

}

console.log(mostSignificantDigit(9999966664443));
console.log(mostSignificantDigit(67.89));
console.log(mostSignificantDigit(0.00987));
