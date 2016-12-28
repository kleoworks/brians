function rotateArr(arr, shiftBy) {

    //shift right
    //outside loop (array - shiftBy) times
    if (shiftBy > 0) {
        for (var i = 0; i < (arr.length - shiftBy); i++) {

            // at each iteration move current value at array index 0 to end of array
            for (var j = 0; j < arr.length - 1; j++) {

                var temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;

            }

        }
    } else {
        for (var i = 0; i < (arr.length - Math.abs(shiftBy)); i++) {

            // at each iteration move current value at array index 0 to end of array
            for (var j = arr.length - 1; j > 0; j--) {

                var temp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = temp;

            }

        }
    }

    return arr;

}

//tests
//shift right (positive)
console.log('shift right');
console.log(rotateArr([1,2,3,4,5,6],1));
console.log(rotateArr([1,2,3,4,5,6],6));
console.log(rotateArr([1,2,3,4,5],2));

//shift left (negative)
console.log('shift left');
console.log(rotateArr([1,2,3,4,5],-2));
