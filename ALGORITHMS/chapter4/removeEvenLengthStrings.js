// change array to remove even length strings but keeping the original general order

function removeEvenLenStrings(arr) {

    for (var i = 0; i < arr.length; i++) {

        if (arr[i].length % 2 == 0) {

            // even string found, must shift all values in array to left by 1, and pop last value
            for (var j = i; j < arr.length - 1; j++) {
                arr[j] = arr[j+1];
            }

            arr.pop();

            // must decrement i, and re-loop again since values have shifted left
            i -= 1;
        }

    }

    return arr;

}

// test
console.log(removeEvenLenStrings(['Nope!', 'Its', 'Kris', 'starting', 'with', 'K!', '(instead', 'of', 'Chris', 'with', 'C)', '.']));
