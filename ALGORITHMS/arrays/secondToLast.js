// eturn the second-to-last element of an array.
// Given [42,true,4,"Liam",7], return "Liam". If array is too short, return null.

function secondToLast(arr) {

    if (arr.length < 2) {
        return null;
    } else {
        return arr[arr.length - 2];
    }

}

//test
console.log(secondToLast([42,true,4,"Liam",7]));
console.log(secondToLast(["Liam", 7]));
console.log(secondToLast(["1 value array returns null"]));
