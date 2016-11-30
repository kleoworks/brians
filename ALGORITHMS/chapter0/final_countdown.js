function finalCountdown(param1, param2, param3, param4) {
    var i = param2;
    while (i < param3) {
        if (i === param4) {
            i++;
            continue;
        }
        if (i % param1 === 0) {
            console.log(i);
        }
        i++
    }
}

//tests
finalCountdown(3,5,17,9);
finalCountdown(5,5,41,35);
