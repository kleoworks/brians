// for [1,3,5,7,9,13], print values greater than 2nd value and return how many values that is

function greaterIndex1 (arr) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > arr[1]) {
            console.log(arr[i]);
            count++;
        }
    }
    return count;
}

//test
var test = greaterIndex1([1,3,5,7,9,13]);
console.log(test);
