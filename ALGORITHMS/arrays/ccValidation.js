function isCreditCardValid(digitArr) {

    // base check if numbers less than 13, not a valid card number
    if (digitArr.length < 13) {
        return false;
    }

    // from 2nd to last index, multiple value by 2 for every other index from back to front
    for (var i = digitArr.length - 2; i >= 0; i-=2) {
        digitArr[i] *= 2;
    }


    // for each index (Except last), if value greater than 9, subtract 9

    for (var i = 0; i < digitArr.length - 1; i+=1) {
        if (digitArr[i] > 9) {
            digitArr[i]-=9;
        }
    }

    //  sum all values including last!
    var sum = 0;
    for (var i = 0; i < digitArr.length; i+=1) {
        sum+= digitArr[i];
    }

    // check if sum is multiple of 10
    if (sum % 10 == 0) {
        return true;
    } else {
        return false;
    }
}

//test
console.log(isCreditCardValid([5,2,2,8,2]));
