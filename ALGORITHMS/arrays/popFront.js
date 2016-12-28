function popFront(arr) {

    if (arr.length > 1) {
        var temp = arr[0];
        arr[0] = arr.pop();
        return temp;
    } else {
        return arr.pop();
    }

}


//tests
console.log(popFront([1,2,3]));
console.log(popFront([10]));
