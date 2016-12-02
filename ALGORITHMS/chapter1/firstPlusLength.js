// return sum of first value in array + array's length.

function sumZeroLength(arr) {
    var sum = arr[0] + arr.length;
    return sum;
}

//tests
var test1 = sumZeroLength([1,2,5,6,7]);
var test2 = sumZeroLength([10,2000,20000]);
var test3 = sumZeroLength(["what?",5,22]);
var test4 = sumZeroLength([false, 5, 22]);

console.log("test1:" + (6 === test1));
console.log("test2:" + (13 === test2));
console.log("test3:" + ("what?3" === test3));
console.log("test4:" + (3 === test4));
