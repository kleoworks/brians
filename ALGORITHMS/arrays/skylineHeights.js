function viewableBuilding(arr) {

    var newarr = [];


    // viewer located at street level / value = 0, each story high = +1
    var max = 0;

    for (var i = 0; i < arr.length; i++) {

        if (arr[i] > max && arr[i] > 0) {
            max = arr[i];
            newarr.push(max);
        }
    }

    return newarr;

}

//tests
console.log(viewableBuilding([-1,7,3]));
console.log(viewableBuilding([-1,1,1,7,3]));
console.log(viewableBuilding([0,4]));
