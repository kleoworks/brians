var HOUR = 12;
var MINUTE = 45;
var PERIOD = "PM";

// create the phrase based on minutes
var phrase1 = "";

if (MINUTE == 5) {
    phrase1 = "5 after";
} else if (MINUTE == 15) {
    phrase1 = "quarter after";
} else if (MINUTE == 30) {
    phrase1 = "half past";
} else if (MINUTE !== 0) {
    if (MINUTE < 30) {
        phrase1 = "just after";
    // else minute is > 30 but not 11!, separate cases for noon and midnight
} else if (HOUR !== 11) {
        phrase1 = "almost";
    }
}

// create the phrase based on PERIOD
var phrase2 = "";

if (PERIOD == "AM") {
    phrase2 = "in the morning";
} else if (PERIOD == "PM") {
    if (HOUR < 6 || HOUR == 12) {
        phrase2 = "in the afternoon";
    } else if (HOUR < 10) {
        phrase2 = "in the evening";
    } else {
        phrase2 = "at night";
    }
}

// if midnight or noon
if (HOUR == 12 && MINUTE == 0) {
    if (PERIOD == "AM") {
        console.log("It's midnight");
    } else {
        console.log("It's noon");
    }
}

// if almost midnight or noon
if (HOUR == 11 && MINUTE > 30) {
    // phrase1 = "";
    if (PERIOD == "PM") {
        console.log("It's almost midnight");
    } else {
        console.log("It's almost noon");
    }
}

// if it's after 12:30am or pm then it's almost 1 in the morning or afternoon, otherwise print all other times
if (HOUR == 12 && MINUTE > 30 && PERIOD == "AM") {
    console.log("It's almost 1 in the morning");
} else if (HOUR == 12 && MINUTE > 30 && PERIOD == "PM") {
    console.log("It's almost 1 in the afternoon");
} else if (phrase1 == "almost") {
    console.log("It's " + phrase1 + " " + (HOUR + 1) + " " + phrase2);
} else if (phrase1 != "") {
    console.log("It's " + phrase1 + " " + HOUR + " " + phrase2);
}
