// Make a function that copies an array, ONLY accepting the items that are numbers.

var myArr = [1, "apple", -3, "orange", 0.5];
var myArr2 = ["bs", "blue", 52, 1, "apple", -3, "orange", 0.5, true, [5,4,"apple"], false, 200];
var myArr3 = [4,5,66,7];

function numbersOnly(arr) {

    var newArr = [];

    for (var i = 0; i < arr.length; i++) {
        if (typeof arr[i] === "number") {
            newArr.push(arr[i]);
        }
    }

    return newArr;

}

// extra... remove any numbers from original array
function noNumbers(arr) {
    for (var i = 0; i < arr.length; i++) {

        while (typeof arr[i] === "number") {

            // if only 1 element left in array, or if reached last element in array and it's a number, remove it
            if (arr.length == 1 || i == arr.length - 1) {
                arr.pop();

            // else replace current element with the last value of array, and repeat loop
            } else {
                arr[i] = arr.pop();
            }
        }
    }
}




//numbers only test
console.log(numbersOnly(myArr));

//no numbers test
noNumbers(myArr2);
console.log(myArr2);
noNumbers(myArr3);
console.log(myArr3);
