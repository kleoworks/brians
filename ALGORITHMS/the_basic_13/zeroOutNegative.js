// Zero Out Negative Numbers
// Return the given array, after setting any negative values to zero.

function zeroNegative(arr) {
    for (var i = 0; i < arr.length; i+=1) {
        if (arr[i] < 0) {
            arr[i] = 0;
        }
    }
    return arr;
}

//tests
console.log(zeroNegative([0,-1,-2,3,5,-5]));
