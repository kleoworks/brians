// Greater than Y
// Given an array and a value Y, count and print the number of array values greater than Y.

function greaterThanY(arr, y) {
        var count = 0;
        for (var i = 0; i < arr.length; i++) {
            if (arr[i] > y) {
                count+=1;
            }
        }
        console.log(count);
}

//test
greaterThanY([1,2,3,4,5],4);
greaterThanY([1,2,3,4,5],0);
