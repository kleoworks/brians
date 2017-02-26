// given two arrays, map first array as keys to second array as values and return object

function zipArray(arrMap, arrVal) {

    my_obj = {};

    if (arrMap.length != arrVal.length) {

        return 'arrays must be of same length'

    } else {

        for (var i = 0; i < arrMap.length; i++) {

            my_obj[arrMap[i]] = arrVal[i];

        }

    }

    return my_obj;

}


// tests
arr1 = ['abc', 3, 'yo'];
arr2 = [42, 'wassup', true];
console.log(zipArray(arr1, arr2));

arr1 = ['abc', 3, 'yo', 4];
arr2 = [42, 'wassup', true];
console.log(zipArray(arr1, arr2));
