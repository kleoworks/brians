function makeItBig(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            arr[i] = "big";
        }
    }
    return arr;
}

//tests
var test1 = makeItBig([-1,3,-2,20,0,-4]);
console.log(test1);
