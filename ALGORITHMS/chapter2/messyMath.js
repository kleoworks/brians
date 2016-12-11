function messyMath(num) {

    var sum = 0;

    for (var i = 0; i <= num; i+=1) {

        if (i == num / 3) {
            return -1;
        } else if (i % 3 === 0) {
            continue;
        } else if (i % 7 === 0) {
            sum+=(i + i);
        } else {
            sum+=i;
        }

    }

    return sum;

}

//tests
console.log(messyMath(4));
console.log(messyMath(8));
console.log(messyMath(15));
