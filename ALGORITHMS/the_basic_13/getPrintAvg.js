// Get and Print Average
// Analyze an array’s values and print the average.

var arr = [1, 2, 3, 4, 5];

var sum = 0;

for (var i = 0; i < arr.length; i+=1) {
    sum+=arr[i];
}

console.log(sum / arr.length);
