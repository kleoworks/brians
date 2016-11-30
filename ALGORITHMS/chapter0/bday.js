function yourBirthday(a, b) {
    if ((a === birthMonth || b === birthMonth) && (a === birthDay || b === birthDay)) {
        console.log("How did you know?");
    } else {
        console.log("Just another day....");
    }
}

var birthMonth = 9;
var birthDay = 3;

// tests
yourBirthday(birthMonth, birthDay);
yourBirthday(9,3);
yourBirthday(3,9);
yourBirthday(birthDay, birthMonth);
yourBirthday(3,4);
yourBirthday(4,3);
yourBirthday(4,9);
yourBirthday(9,4);
