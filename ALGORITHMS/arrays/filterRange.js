function filterRange(arr, min, max) {

    // remove values between min and max, keeping array intact

    for (var i = 0; i < arr.length; i++) {
        //overwrite value with next value in array, and shift all values left 1 index, pop last value

        if (arr[i] > min && arr[i] < max) {

            for (var j = i; j < arr.length; j++) {
                if (j == arr.length - 1) {
                    arr.pop();
                } else {
                    arr[j] = arr[j+1];
                }
            }

            // decrement i to recheck current index again at next iteration since values have shifted
            i-=1;
        }

    }

    return arr;
}


//tests
console.log(filterRange([0,1,2,3,4,5], 1, 4));
console.log(filterRange([5,3,1,2,2,2,2], 1, 4));
console.log(filterRange([0,2], 1, 4));
console.log(filterRange([2,0], 1, 4));
