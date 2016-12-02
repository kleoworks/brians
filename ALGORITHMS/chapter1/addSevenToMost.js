function addSeven(arr) {
    var newarr = [];
    for (var i = 1; i < arr.length; i++) {
        newarr.push(arr[i]+7);
    }
    return newarr;
}

//tests
var test1 = addSeven([1,3,5,6]);
console.log(test1); // return [10,12,13]
