function printLow(arr) {
    var min = arr[0];
    var max = arr[0];
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    console.log(min);
    return max;
}

//tests min
var test1 = printLow([1,4,7,9]); // print 1
var test2 = printLow([9,3,20,-1]); // print -1
var test3 = printLow([90,200]); // print 90
//tests max
console.log(test1); // print 9
console.log(test2); // print 20
console.log(test3); // print 200
