function rollOne() {
    // return random Int 1 - 6
    return Math.ceil(Math.random()*(7-1));
}


function playFives(num) {
    for (var i = 0; i < num; i++) {
        var roll = rollOne();
        if (roll == 5) {
            console.log("5", "That's good luck!");
        } else {
            console.log(roll);
        }
    }
}


function playStatistics() {
    var max = 0; // set max below min random Int to start
    var min = 7; // set minimum above max random Int to start

    for (var i = 0; i < 8; i++) {

        var roll = rollOne();

        if (roll > max) {
            max = roll;
        } else if (roll < min) {
            min = roll;
        }

    }

    console.log("Max: ", max, "Min: ", min);
}


function playStatistics2() {
    var max = 0; // set max below min random Int to start
    var min = 7; // set minimum above max random Int to start
    var sum = 0;

    for (var i = 0; i < 8; i++) {

        var roll = rollOne();
        sum += roll;

        if (roll > max) {
            max = roll;
        } else if (roll < min) {
            min = roll;
        }

    }

    console.log("Max: ", max, "Min: ", min, "Sum: ", sum);
}


function playStatistics3(num) {
    var max = 0; // set max below min random Int to start
    var min = 7; // set minimum above max random Int to start
    var sum = 0;

    for (var i = 0; i < num; i++) {

        var roll = rollOne();
        sum += roll;

        if (roll > max) {
            max = roll;
        } else if (roll < min) {
            min = roll;
        }

    }

    console.log("Max: ", max, "Min: ", min, "Sum: ", sum);
}


function playStatistics4(num) {
    var max = 0; // set max below min random Int to start
    var min = 7; // set minimum above max random Int to start
    var sum = 0;

    for (var i = 0; i < num; i++) {

        var roll = rollOne();
        sum += roll;

        if (roll > max) {
            max = roll;
        } else if (roll < min) {
            min = roll;
        }

    }

    console.log("Max: ", max, "Min: ", min, "Avg: ", sum / num);
}



//test
playStatistics4(2);
