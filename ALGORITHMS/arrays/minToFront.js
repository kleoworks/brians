function minToFront(arr) {

    var min = arr[0];
    var index = 0;

    //iterate through array, find minimum value and store index
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
            index = i;
        }
    }

    //use index, and swap values in reverse.
    for (var i = index; i > 0; i--) {
        var temp = arr[i];
        arr[i] = arr[i-1];
        arr[i-1] = temp;
    }

    return arr;

}

//test
console.log(minToFront([4,2,1,3,5]));
console.log(minToFront([4,2,7,12,14,19,1,0,3,5]));
