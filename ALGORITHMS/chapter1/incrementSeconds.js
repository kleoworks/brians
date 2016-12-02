function increment2ndElement(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (i % 2 !== 0) {
            arr[i]+=1;
        }
        console.log(arr[i]);
    }
    return arr;
}

//tests
var test1 = increment2ndElement([0,2,4,5,8,0,1]);
console.log(test1);
