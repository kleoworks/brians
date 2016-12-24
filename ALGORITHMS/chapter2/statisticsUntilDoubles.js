function twentySidedDie() {

    var max = 0; // set max less than min random Int to start
    var min = 21; // set min greater than max random Int to start
    var sum = 0;
    var count = 0;
    var lastRoll = 0;

    while(true) {

        var roll = rollDie();
        sum+=roll;
        count+=1;

        // check min and max
        if (roll > max) {
            max = roll;
        } else if (roll < min){
            min = roll;
        }

        // check if last roll is same as current roll, if it is then display stats and exit
        if (roll == lastRoll) {
            console.log('# of rolls: ', count, 'Min: ', min, 'Max: ', max, 'Avg: ', sum / count);
            return;

        } else {
            lastRoll = roll;
        }

    }

}

// roll die
function rollDie() {
    return Math.ceil(Math.random()*20);
}


twentySidedDie();
