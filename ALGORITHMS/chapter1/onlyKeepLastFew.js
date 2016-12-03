function keepLastFew(arr, num) {
    arr = arr.slice(arr.length - num, arr.length);
    return arr;
}

//test
console.log(keepLastFew([2,4,6,8,10],3));
console.log(keepLastFew([2,4,6,8,10],0));
console.log(keepLastFew([1,2,3],2));
