function clockHandAngles(seconds) {

    //given # in seconds since 12:00:00, print in degrees hour, minute and seconds

    //week hand for each week

    var clockSeconds = {
        week: 604800,
        hour: 3600,
        min: 60,
        sec: 1
    }

    var clockDegrees = {
        week: 0,
        hour: 0,
        min: 0,
        sec: 0
    }


    clockDegrees.week = ((seconds * .00059523809) % 360) + ' degs';

    clockDegrees.hour = Math.floor(seconds / clockSeconds.hour);
    seconds = Math.abs(clockDegrees.hour * clockSeconds.hour - seconds);

    clockDegrees.min = Math.floor(seconds / clockSeconds.min);
    seconds = Math.abs(clockDegrees.min * clockSeconds.min - seconds);

    clockDegrees.sec = seconds;

    clockDegrees.hour = ((clockDegrees.hour * 30) % 360) + (.5 * (clockDegrees.min + (clockDegrees.sec / 60))) + ' degs';
    clockDegrees.min = (clockDegrees.min * 6) + (.1 * clockDegrees.sec) + ' degs';
    clockDegrees.sec = (clockDegrees.sec * 6) + ' degs';

    console.log('Week Hand: ' + clockDegrees.week + '. Hour Hand: ' + clockDegrees.hour + '. Minute Hand: ' + clockDegrees.min + '. Second Hand: ' + clockDegrees.sec + '.');
}

//test
clockHandAngles(3600);
clockHandAngles(119730);
