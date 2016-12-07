// Find and Print Max
// Given an array, find and print its largest element.

var arr = [1,2,3,4,5,0,2,10];

var max = 0;

for (var i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
        max = arr[i];
    }
}

console.log(max);
