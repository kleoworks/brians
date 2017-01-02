// don't use nested loops

function removeNegatives(arr) {

    var found_neg = false;
    var neg_idx = 0;

    for (var i = 0; i < arr.length; i++) {

        if (arr[i] < 0 && i != arr.length - 1) {
            var temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;

            if (found_neg == false) {

                neg_idx = i; // when loop has iterated over array, restart at this index
                found_neg = true; // since you found a negative, you will need to reloop over this array until all negatives are removed
            }

        } else if (arr[i] < 0 && i == arr.length - 1) {
            arr.pop();
        }

        // check if found neg, and then reset i to reloop over array
        if (i == arr.length && found_neg == true) {
            found_neg = false;
            i = neg_idx - 1;
        }

    }

    return arr;
}

//test
console.log(removeNegatives([0, 1, 2, -3, 4, -5, 6]));
console.log(removeNegatives([0, -1, -2, -3, -4, -5, 6]));
console.log(removeNegatives([-1, -1, -2, -3, -4, -5]));
console.log(removeNegatives([0]));
