function swapTowardCenter(arr) {
    var temp = arr[arr.length-1];
    arr[arr.length-1] = arr[0];
    arr[0] = temp;

    temp = arr[arr.length-3];
    arr[arr.length-3] = arr[2];
    arr[2] = temp;

    return arr;
}

//test
console.log(swapTowardCenter([1,2,3,4,5,6]));
console.log(swapTowardCenter([true,42,"Ada",2,"pizza"]));
