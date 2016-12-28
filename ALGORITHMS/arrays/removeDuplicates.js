function removeDuplicates(arr) {

    var noDupesArr = [];
    var index = 0;

    for (var i = 0; i < arr.length-1; i++) {

        console.log('top of loop i is:', i);
        if (arr[i] != arr[i+1]) {
            noDupesArr[index] = arr[i];
            index++;
            if (i == arr.length - 2) {
                noDupesArr[index] = arr[i+1];
            }
        }

    }

    return noDupesArr;

}

//tests
console.log(removeDuplicates([1,2,3,"a","a","b","b","brian","brian","last value"]));
