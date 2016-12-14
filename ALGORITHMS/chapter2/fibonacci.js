function fibonacci(num) {

    //first two given values, fibonacci(0) = 0, fibonacci(1) = 1
    var arr = [0,1];
    for (var i = 1; i < num; i++) {
        arr.push(arr[i]+arr[i-1]);
    }
    return arr[num];
}

//tests
console.log(fibonacci(5));
console.log(fibonacci(6));
console.log(fibonacci(7));
