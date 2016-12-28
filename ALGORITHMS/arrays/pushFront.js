function pushFront(arr, val) {
    arr[arr.length] = arr[0];
    arr[0] = val;
    return arr;
}

//test
console.log(pushFront([25,32,4],"inserted!"));
