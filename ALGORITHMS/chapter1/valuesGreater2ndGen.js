// for any array, return new array with only the values greater than 2nd value and print how many values that is

function greaterIndex1 (arr) {

    if (arr.length > 1) {
        var newarr = [];
        var count = 0;
        for (var i = 0; i < arr.length; i++) {
            if (arr[i] > arr[1]) {
                newarr.push(arr[i]);
                count++;
            }
        }
        console.log(count);
        return newarr;
        }
    }

//tests
var test = greaterIndex1([1,3,5,7,9,13]);
console.log(test);

var test2 = greaterIndex1([10,1]);
console.log(test2);

var test3 = greaterIndex1([20,3,1,1,1,1,2,3,4,]);
console.log(test3);
