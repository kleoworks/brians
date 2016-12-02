function replaceLastValue(arr) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            count++;
        }
    }
    arr[arr.length-1] = count;
    return arr;
}

//test
var test1 = replaceLastValue([-1,-3,-5,2,2,3,8,-123,0]);
console.log(test1);
//should print [-1,-3,-5,2,2,3,8,-123, 4]
