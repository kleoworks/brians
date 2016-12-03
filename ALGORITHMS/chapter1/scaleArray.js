function scaleArray(arr, num) {
    for (var i = 0; i < arr.length; i++) {
        arr[i]*=num;
    }
    return arr;
}

console.log(scaleArray([1,2,3,4,5], 1));
console.log(scaleArray([1,2,3,4,5], 0));
console.log(scaleArray([1,2,3,4,5], 10));
