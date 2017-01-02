// Array: Nth-to-Last
// Return the element that is N-from-array’s-end. Given ([5,2,3,6,4,9,7],3), return 4. If the array is too short, return null.

function nthToLast(arr, nth) {

    if (arr.length < nth) {
        return null;
    } else {
        return arr[arr.length - nth];
    }

}

//test
console.log(nthToLast([5,2,3,6,4,9,7],3));
console.log(nthToLast([5,2,3,6,4,9,7],8));
