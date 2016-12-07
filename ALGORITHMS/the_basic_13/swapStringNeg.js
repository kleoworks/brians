// Swap String For Array Negative Values
// Given an array of numbers, replace any negative values with the string 'Dojo'.


var arr = [1,2,3,-1,-10,5,-100];

for (var i = 0; i < arr.length; i+=1) {
    if (arr[i] < 0) {
        arr[i] = 'Dojo';
    }
}

console.log(arr);
