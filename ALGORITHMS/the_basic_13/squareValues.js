// Square the Values
// Square each value in a given array, returning that same array with changed values.

var arr = [1, 2, 3, 4, 5];

for (var i = 0; i < arr.length; i+=1) {
    arr[i]*=arr[i];
}

//test
console.log(arr);
