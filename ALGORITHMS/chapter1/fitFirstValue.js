// if array[0] > array.length, print "Too big!"
// if array[0] < array.length, print "Too small!"
// otherwise print "Just right!"

function fitValue (arr) {
    arr[0] > arr.length ? console.log("Too big!") : arr[0] < arr.length ? console.log("Too small!") : console.log("Just right!");
}

//tests
fitValue([1,3,5]);
fitValue([5,3,1]);
fitValue([3,2,2]);
