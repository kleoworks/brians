// for given array return a string of comma separated values.  if values are consecutive then show as a range i.e. for [1, 36,37,38] return string "1, 36-38"

// this function exploits the fact that javascript does not error out on out-of-range indices
// come back to this and improve it!!!!!!

function bookIndex(arr) {

    var last_val = arr[0];
    var temp_arr = [last_val];
    var new_arr = [];

    for (var i = 1; i <= arr.length; i++) {

        if (arr[i] - 1 == last_val) {
            temp_arr.push(arr[i]);

        } else {

            if (temp_arr.length > 1) {

                var sequence = temp_arr[0] + "-" + temp_arr[temp_arr.length-1];
                new_arr.push(sequence)
                temp_arr = [arr[i]]

            } else if (temp_arr.length == 1) {

                new_arr.push(temp_arr[0])
                temp_arr = [arr[i]]

            } else if (temp_arr.length == 0) {

                temp_arr.push(arr[i])

            }

        }

        last_val = arr[i]

    }

    return new_arr.join(', ')

}


// test
console.log(bookIndex([1,13,14,15,37,38,70]));
console.log(bookIndex([1,13,14,15,37,38,39]));
