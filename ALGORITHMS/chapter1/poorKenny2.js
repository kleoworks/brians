function whatReallyHappensToday(volcano, tsunami, earthquake, blizzard, meteor) {

    var catastrophe = ["volcano", "tsunami", "earthquake", "blizzard", "meteor strike"];

    for (var i = 0; i < arguments.length; i++){
        if (arguments[i] > 0) {
            console.log(arguments[i] * 100 + "% chance of a " + catastrophe[i]);
        }
    }
}

//test
whatReallyHappensToday(.10, .15, .20, .25, .30);
whatReallyHappensToday(.10, 0, .20, 0, 0);
