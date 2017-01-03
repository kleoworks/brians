function shuffle(arr) {

    function randomGen(arrLength) {
        return Math.floor(Math.random()*(arrLength - 0));
    }

    for (var i = 0; i < arr.length; i++) {

        var random = randomGen(arr.length);
        var temp = arr[random];
        arr[random] = arr[i];
        arr[i] = temp;

    }

    return arr;

}

//test
console.log(shuffle([1,2,3,4,5]));
console.log(shuffle([6,7,8,9,10]));
