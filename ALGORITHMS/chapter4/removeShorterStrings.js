// given a string Array and value (length), remove any strings shorter than length of the array
// 5m


function removeShorterStrings(arr, length) {

    for (var i = 0; i < arr.length; i++) {

        if (arr[i].length > length) {

            arr[i] = arr.pop();
            i-=1

        }

    }

    return arr;

}

//tests
arr1 = ['Brian', 'Joe', 'Josephine', 'Briana', 'Jack', 'Melissa', 'Tony', 'Courtney', 'Jackson'];
console.log(removeShorterStrings(arr1, 5));
