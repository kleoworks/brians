function letterGrade(num) {
    if (num >= 90) {
        console.log("Score:" + num + ". Grade: A");
    } else if (num >= 80) {
        console.log("Score:" + num + ". Grade: B");
    } else if (num >= 70) {
        console.log("Score:" + num + ". Grade: C");
    } else if (num >= 60) {
        console.log("Score:" + num + ". Grade: D");
    } else {
        console.log("Score:" + num + ". Grade: F");
    }

}

//tests
letterGrade(81);
letterGrade(91);
letterGrade(0);
