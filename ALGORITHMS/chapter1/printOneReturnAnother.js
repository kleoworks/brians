function printAndReturn(arr) {
    console.log(arr[arr.length - 2]); // print 2nd to last value
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 !== 0) {
            return arr[i]; // return first odd value
        }
    }
}

//test
var test1 = printAndReturn([2,6,20,12,7,9]); // prints 7
var test2 = printAndReturn([19,2,4,3]); // prints 4

console.log(test1); // prints 7
console.log(test2); // prints 19
