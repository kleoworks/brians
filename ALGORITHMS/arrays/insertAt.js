function insertAt(arr, index, val) {

    if (index < 0) {
        //can't add to an array with a negative index
        return;
    } else if (arr.length == 0 || index > arr.length - 1) {
        //set index without swapping values if an empty array or if index is greater than last index
        arr[index] = val;
    } else {
        var temp = arr[index];
        arr[index] = val;
        arr[arr.length] = temp;
    }

    return arr;
}

//tests
console.log(insertAt([],2,"inserted"));
console.log(insertAt([1,2],2,"inserted"));
console.log(insertAt([1,2],0,"inserted"));
