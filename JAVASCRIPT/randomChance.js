var wonAmt = 0;

function playSlots(quarter, playUntil) {

    while (quarter > 0 && quarter <= playUntil) {
        quarter-=1;
        console.log("gambling....")

        // check if 2 randomly generated numbers are equal
        if (Math.floor((Math.random()*100)) === (Math.floor((Math.random()*100)))) {
            // give random amount of quarters if won!
            wonAmt = Math.floor((Math.random()*50)+51);
            quarter += wonAmt;
            console.log("you won " + wonAmt + " quarters!");
            console.log("you now have " + quarter + " quarters!");
        }
    }
    if (quarter == 0) {
        console.log("game over - you're out of quarters");
        return 0;
    }
    console.log("you lucky dog, you made what you wanted")
    return quarter;
}

playSlots(150, 200);
