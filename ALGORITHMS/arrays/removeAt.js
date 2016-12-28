function removeAt(arr,index) {

    if (index < 0 || index > arr.length - 1) {
        return;
    } else {
        var temp = arr[index];
        arr[index] = arr[arr.length - 1];
        arr[arr.length - 1] = temp;
        arr.pop();
    }
    return arr;
}

//tests
console.log(removeAt([1,2,3],1));
console.log(removeAt([1,2,3],0));
