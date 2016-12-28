function reverse(arr) {

    var reverseIndex = arr.length - 1;

    for (var i=0; i<arr.length; i++) {
        if (i >= reverseIndex) {
            break;
        } else {
            var temp = arr[reverseIndex];
            arr[reverseIndex] = arr[i];
            arr[i] = temp;
        }
        reverseIndex-=1;
    }

    return arr;

}


//test
console.log(reverse([1,2,3,4,5]));
