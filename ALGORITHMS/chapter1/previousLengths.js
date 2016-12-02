function replacePrevious(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
        arr[i] = arr[i-1].length;
    }
    return arr;
}

//test
var test1 = replacePrevious(["string1", "str2", "string-3", "str-4"]);
console.log(test1);
