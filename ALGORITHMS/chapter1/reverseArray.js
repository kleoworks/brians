function reverseArray(arr) {
    var temp = 0;
    var j = arr.length - 1;
    for (var i = 0; i < arr.length; i++) {
        if (j > i) {
            temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
            j--;
        }
    }
    return arr;
}

//tests
var test1 = reverseArray([1,2,5,6,7,8,9]);
var test2 = reverseArray([1,2,6,8]);
var test3 = reverseArray([9,5]);
console.log(test1);
console.log(test2);
console.log(test3);
