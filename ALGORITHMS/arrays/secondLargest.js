// Return the second-largest element of an array.
// Given [42,1,4,Math.PI,7], return 7. If the array is too short, return null.


function secondLargest(arr) {

    var first = arr[0];
    var second = null;

    if (arr.length < 2) {
        return null;
    } else {

        for (var i = 0; i < arr.length; i++) {

            if (second == null) {
                if (arr[i] < first) {
                    second = arr[i];
                } else if (arr[i] > first) {
                    first = arr[i];
                }
            } else {
                if (arr[i] > first) {
                    first = arr[i];
                } else if (arr[i] > second) {
                    second = arr[i];
                }
            }
        }
    }
    return second;
}

//test
console.log(secondLargest([42,1,4,Math.PI,7]));
console.log(secondLargest([43,43,42,Math.PI,7]));
console.log(secondLargest([43,43,43])); //returns null if there is no 2nd largest value!
