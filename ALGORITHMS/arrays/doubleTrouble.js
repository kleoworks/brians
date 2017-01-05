function doubleTrouble(arr) {

    for (var i = 0; i < arr.length; i+=2) {

        //shift values right +1 in array
        for (var j = arr.length; j > i; j-=1) {

            arr[j] = arr[j-1];

        }

        // duplicate value
        arr[i+1] = arr[i];
    }

    return arr;

}


//tests
console.log(doubleTrouble([4,"Ulysses",42,false]));
console.log(doubleTrouble([4,"Ulysses",42]));
console.log(doubleTrouble([4,"Ulysses"]));
console.log(doubleTrouble([4]));
