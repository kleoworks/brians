function nthLargest(arr, n) {

    var swap = false;
    var sorted = false;

    //sort array! high to low
    for (var i = 0; i < arr.length; i++) {

        if (i == arr.length - 1 && swap == true) {
            swap = false;
            // set i to -1, so at next iteration it will return to zero and loop over array again
            i = -1;
        } else if (i == arr.length - 1 && swap == false) {
            sorted = true;
        } else if (arr[i] < arr[i+1]) {
            //swap
            var temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
            swap = true;
        }

        if (sorted == true) {
            break;
        }

    }


    //get the nth largest value in a sorted array !
    var j = 0; // increment by j
    var counter = 0; // this counts how many times in a sorted array the next index value is smaller than current index

    while (true) {

        // if counter reaches n-1, nthLargest value has been found!
        if (counter == (n - 1) ) {
            return arr[j];
        } else if (arr[j] > arr[j+1]) {
            counter+=1;
        // if reached end of array and counter does not equal n-1, return null
        } else if (j == arr.length - 1 && counter != (n-1)) {
            return null;
        }
        j+=1;
    }

}

//test sort
console.log(nthLargest([1,2,3,4,5,6,7,8,9,10,10,10,10,1], 2));
console.log(nthLargest([1,2,3,4,5,6,7,8,9,10,10,10,10,1], 4));
console.log(nthLargest([10,10,10,10], 1));
console.log(nthLargest([10,10,10,10], 2));
