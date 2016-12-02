// create array from counting down from num to 0

function Countdown(num) {
    var arr = [];
    for (var i = num; i >= 0; i--) {
        arr.push(i);
    }
    console.log(arr);
}

//test
Countdown(40);
