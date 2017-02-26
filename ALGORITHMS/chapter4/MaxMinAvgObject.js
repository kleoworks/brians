// given array, return an object containing the max min and avg values

function objectVals(arr) {


    var obj_vals = {

        min: minimum(arr),
        max: maximum(arr),
        avg: average(arr)

    }

    function minimum(arr) {

        var min = arr[0];

        for (var i = 0; i < arr.length; i++) {

            if (arr[i] < min) {

                min = arr[i]

            }

            return min;

        }

    }


    function maximum(arr) {

        var max = arr[0];

        for (var i = 0; i < arr.length; i++) {

            if (arr[i] > max) {

                max = arr[i];

            }

        }

        return max;

    }

    function average(arr) {

        sum = 0;

        for (var i = 0; i < arr.length; i++) {

            sum+=arr[i];

        }

        return sum / arr.length;

    }

    return obj_vals;


}

console.log(objectVals([2,3,5,7]).min);
console.log(objectVals([2,3,5,7]).max);
console.log(objectVals([2,3,5,7]).avg);
