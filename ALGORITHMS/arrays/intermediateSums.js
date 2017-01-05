// After every tenth element, add an additional element containing the sum of those ten values
// If the array does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet been included in one of the earlier sums.
// Given the array [1,2,1,2,1,2,1,2,1,2,1,2,1,2], change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6].

function intermediateSums(arr) {

    var i  = 0;
    var counter = 0;
    var sum = 0;


    while (i <= arr.length) {

        sum += arr[i];
        counter++;
        i++;

        // if you've summed 10 indices, and there are more indices left in array, shift remaining values in array over + 1 to make space to insert value of sum
        if (counter == 10 && i < arr.length) {

            for (var j = arr.length; j > i; j-=1) {

                arr[j] = arr[j-1];

            }

            // insert sum and reset counter and sum
            arr[i] = sum;
            counter = 0;
            sum = 0;


            // increment i to next index to start summing next 10 (or less) indices at start of next iteration
            i++;


        // insert sum at the end of the array and return array
        } else if (i == arr.length) {

            arr[i] = sum;
            return arr;

        }


    }

}

//test
console.log(intermediateSums([1,2,1,2,1,2,1,2,1,2,1,2,1,2]));
console.log(intermediateSums([1,2,1,2,1,2,1,2,1,2,1]));
console.log(intermediateSums([1,2,1,2,1,2,1,2,1,2]));
console.log(intermediateSums([1,2,1,2,1]));
console.log(intermediateSums([0,1]));
