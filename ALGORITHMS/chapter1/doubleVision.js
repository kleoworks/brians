function doubleArray(arr) {
    var arrnew = [];
    for (var i = 0; i < arr.length; i++) {
        arrnew.push(arr[i]*2);
    }
    return ("arr " + arr + ", arrnew " + arrnew);
}

//test
var test1 = doubleArray([1,3,4,7]);
console.log(test1);
