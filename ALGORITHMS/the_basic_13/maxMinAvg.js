// Max, Min, Average
// Given an array, print the max, min and average values for that array.

var arr = [1,2,3,4,5];

var max = arr[0];
var min = arr[0];
var sum = 0;

for (var i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
        max = arr[i];
    }
    if (arr[i] < min) {
        min = arr[i];
    }
    sum += arr[i];
}

console.log("max: " + max);
console.log("min: " + min);
console.log("avg: " + (sum / arr.length));
