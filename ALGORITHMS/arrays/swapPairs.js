function swapPairs(arr) {

    if (arr.length <= 1) {
        return arr;
    } else if (arr.length % 2 == 0) {

        for (var i = 0; i < arr.length; i+=2) {
            var temp = arr[i+1];
            arr[i+1] = arr[i];
            arr[i] = temp;
        }
    } else {

        for (var i = 0; i < arr.length - 1; i+=2) {
            var temp = arr[i+1];
            arr[i+1] = arr[i];
            arr[i] = temp;
        }

    }
    return arr;
}

//tests
console.log(swapPairs(["Brendan"]));
console.log(swapPairs(["Brendan",true]));
console.log(swapPairs([1,2,3,4]));
console.log(swapPairs(["Brendan",true,42]));
console.log(swapPairs(["Brendan",true,42,"Brian","Joe",5]));
