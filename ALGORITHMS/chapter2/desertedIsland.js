function weekdayName(weekdayNum) {

    switch (weekdayNum) {

        case 1:
            console.log('Sunday');
            break;
        case 2:
            console.log('Monday');
            break;
        case 3:
            console.log('Tuesday');
            break;
        case 4:
            console.log('Wednesday');
            break;
        case 5:
            console.log('Thursday');
            break;
        case 6:
            console.log('Friday');
            break;
        case 7:
            console.log('Saturday');
            break;
        default:
            break;
    }
}

function weekdayName2(weekdayNum) {

    var num = weekdayNum % 7;

    switch (num) {
        case 1:
            return 'Sunday';
        case 2:
            return 'Monday';
        case 3:
            return 'Tuesday';
        case 4:
            return 'Wednesday';
        case 5:
            return 'Thursday';
        case 6:
            return 'Friday';
        case 0:
            return 'Saturday';
        default:
            break;
    }
}

function someDays() {

    for (var i = 0; i < 17; i++) {
        var randNum = Math.ceil(Math.random()*365);
        var day = weekdayName2(randNum);
        if (day == "Saturday" || day == "Sunday") {
            console.log(day, 'Enjoy your day off!');
        } else {
            console.log(day, 'Work hard!');
        }
    }
}


function monthName(monthNum) {

    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

    return months[monthNum - 1];

}

function monthToDays(monthNum) {

    switch (monthNum) {
        case 1:
            return 31;
        case 2:
            return 28;
        case 3:
            return 31;
        case 4:
            return 30;
        case 5:
            return 31;
        case 6:
            return 30;
        case 7:
            return 31;
        case 8:
            return 31;
        case 9:
            return 30;
        case 10:
            return 31;
        case 11:
            return 30;
        case 12:
            return 31;
        default:
            break;
    }
}

function monthToDaysLeap(monthNum) {

    switch (monthNum) {
        case 1:
            return 31;
        case 2:
            return 29;
        case 3:
            return 31;
        case 4:
            return 30;
        case 5:
            return 31;
        case 6:
            return 30;
        case 7:
            return 31;
        case 8:
            return 31;
        case 9:
            return 30;
        case 10:
            return 31;
        case 11:
            return 30;
        case 12:
            return 31;
        default:
            break;
    }
}

function dayToMonth(dayNum) {

    var date = dayNum;

    for (var i = 1; i <=12; i++) {
        date -= monthToDays(i);
        if (date <= 0) {
            return monthName(i);
        }
    }
}

function dayToMonthLeap(dayNum) {

    var date = dayNum;

    for (var i = 1; i <=12; i++) {
        date -= monthToDaysLeap(i);
        if (date <= 0) {
            return monthName(i);
        }
    }
}

function fullDate(dayNum) {
    var date = dayNum;
    for (var i = 1; i <=12; i++) {
        date -= monthToDays(i);
        if (date <= 0) {
            date+=monthToDays(i);
            return weekdayName2(dayNum) + ", " + dayToMonth(dayNum) + " " + date + ", 2017";
        }
    }
}

function fullDate2(dayNum) {

    var year = 2017;
    var date = dayNum;

    function parseDate(days) {
        var date = days;

        if (year % 4 != 0) {

            //non leap year
            for (var i = 1; i <=12; i++) {
                date -= monthToDays(i);
                if (date <= 0) {
                    date+=monthToDays(i);
                    return weekdayName2(dayNum) + ", " + dayToMonth(days) + " " + date + ", " + year;
                }
            }

        } else {

            //leap year
            for (var i = 1; i <=12; i++) {
                date -= monthToDaysLeap(i);
                if (date <= 0) {
                    date+=monthToDaysLeap(i);
                    return weekdayName2(dayNum) + ", " + dayToMonthLeap(days) + " " + date + ", " + year;
                }
            }
        }
    }


    while (true) {

        if (date <= 365 || (date <= 366 && year % 4 == 0)) {
            //not a leap year... passing (date - 1) since counting from 12/31/16, not 1/1/17

            return parseDate(date);

        } else if (year % 4 != 0) {
            date -= 365;
        } else {
            date -= 366;
        }

        year += 1;

    }

}


function fullDate3(dayNum) {

    var year = 2017;
    var date = dayNum;

    function parseDate(days) {

        var date = days;

        //if non leap year
        if (year % 4 != 0 || (year % 100 == 0 && year % 400 != 0)) {
            for (var i = 1; i <=12; i++) {
                date -= monthToDays(i);
                if (date <= 0) {
                    date+=monthToDays(i);
                    return weekdayName2(dayNum) + ", " + dayToMonth(days) + " " + date + ", " + year;
                }
            }

        } else {
            //else leap year
            for (var i = 1; i <=12; i++) {
                date -= monthToDaysLeap(i);
                if (date <= 0) {
                    date+=monthToDaysLeap(i);
                    return weekdayName2(dayNum) + ", " + dayToMonthLeap(days) + " " + date + ", " + year;
                }
            }
        }
    }


    while (true) {

        if (date <= 365 || (date <= 366 && (year % 4 == 0 && year % 100 != 0)) || (date <= 366 && (year % 400 == 0))) {
            return parseDate(date);
        } else if (year % 4 != 0 || (year % 100 == 0 && year % 400 != 0)) {
            date -= 365;
        } else {
            date -= 366;
        }

        year += 1;

    }

}



//tests
// weekdayName(7);
// console.log(weekdayName2(7));
// console.log(weekdayName2(20));
// someDays();
// console.log(monthName(12));
// console.log(monthToDays(2));
// console.log(dayToMonth(75));
// console.log(dayToMonth(91));
// console.log(fullDate(142));
console.log(fullDate2(8475));
console.log(fullDate3(139947));
