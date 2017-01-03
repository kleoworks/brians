function removeRange(arr, start, end) {

    // if end range is the last index, pop the values up to and including start range
    if (end == arr.length - 1) {
        for (var i = end; i >= start; i-=1) {
            arr.pop();
        }
    } else {

        for (var i = end; i >= start; i--) {
            //shift unwanted values to end of array starting from end value working in reverse
            for (var j = i; j < arr.length - 1; j++) {
                var temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
            //pop it!
            arr.pop();
        }

    }

    return arr;

}


//tests
//best case range is at end of array
console.log(removeRange([0,1,2,3,4,5],3,5));

console.log(removeRange([0,1,2,3,4,5],1,2));
