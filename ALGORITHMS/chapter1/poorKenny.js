function whatHappensToday(volcano, tsunami, earthquake, blizzard, meteor) {

    var catastrophe = ["volcano", "tsunami", "earthquake", "blizzard", "meteor strike"];

    var max = 0;
    var index = 0;

    for (var i = 0; i < arguments.length; i++){
        if (arguments[i] > max) {
            max = arguments[i];
            index = i;
        }
    }
    console.log(arguments[index] * 100 + "% chance of a " + catastrophe[index]);
}

//test
whatHappensToday(.10, .15, .20, .25, .30);
