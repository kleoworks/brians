function evenAndOdd(arr) {
    var even = 0;
    var odd = 0;

    for (var i = 0; i < arr.length; i++) {

        if (arr[i] === 0) {
            continue;
        }

        if (arr[i] % 2 === 0) {
            odd = 0;
            even++;
        }
        if (arr[i] % 2 !== 0) {
            even = 0;
            odd++;
        }
        if (odd === 3) {
            console.log("That's odd!");
            odd = 0;
        }

        if (even === 3) {
            console.log("Even more so!");
            even = 0;
        }

    }
}

//tests
var test1 = [1,2,1,3,5,5,5,2,4,6,0,1,1,2,1,1,-1];
evenAndOdd(test1);
