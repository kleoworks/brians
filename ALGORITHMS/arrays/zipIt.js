function zipIt(arr1, arr2) {

    arrLength = arr1.length + arr2.length;
    var newArr = [];

    for (var i = 0; i < arrLength; i++) {

        if (i < arr1.length) {

            newArr.push(arr1[i]);

        }

        if (i < arr2.length) {

            newArr.push(arr2[i]);

        }

    }

    return newArr;

}

//tests
console.log(zipIt([1,2],[10,20,30,40]));
console.log(zipIt([10,20,30,40],[1,2]));
console.log(zipIt([10],[1]));
