function makeNegative(arr) {
    var newarr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            newarr.push(arr[i] * -1);
        }
        else {
            newarr.push(arr[i]);
        }
    }
    return newarr;
}

//tests
var test1 = makeNegative([1,3,5,0,-5,-7]);
var test2 = makeNegative([0]);
var test3 = makeNegative([0,1,-1,2,-5]);

console.log(test1);
console.log(test2);
console.log(test3);
