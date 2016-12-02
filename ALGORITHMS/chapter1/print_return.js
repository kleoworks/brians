// receive array with two numbers.  prints first value, return second

function printArray (arr) {
    console.log(arr[0]);
    return arr[arr.length-1];
}

//tests
var secondValue = printArray([50,2]);
console.log(secondValue);
