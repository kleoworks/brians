var myArr = ["James", "Jill", "Jane", "Jack"];


function printArray(arr) {
    for (var i = 0; i < arr.length; i+=1) {
        console.log(i + " -> " + arr[i]);
    }
}

//test
printArray(myArr);

// fancyArray extra

function printArrayXXX(arr, str, rev) {
    if (rev === true) {
        for (var i = arr.length - 1; i >= 0; i-=1) {
            console.log(i + " " + str + " " + arr[i]);
        }
    } else {
        for (var i = 0; i < arr.length; i+=1) {
            console.log(i + " " + str + " " + arr[i]);
        }
    }
}

printArrayXXX(myArr, "~");
printArrayXXX(myArr, ">>>", true);
