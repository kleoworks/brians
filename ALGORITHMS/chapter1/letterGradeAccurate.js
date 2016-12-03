function letterGrade(grade) {

    if (grade >= 60 && grade <= 92) {
        var num = grade.toString().charAt(1);
        var sym = num >= 0 && num <= 2 ? "-" : num >= 8 && num <= 9 ? "+" : "";
    } else { sym = "";}

    if (grade >= 90) {
        console.log("Score:" + grade + ". Grade: A" + sym);
    } else if (grade >= 80) {
        console.log("Score:" + grade + ". Grade: B" + sym);
    } else if (grade >= 70) {
        console.log("Score:" + grade + ". Grade: C" + sym);
    } else if (grade >= 60) {
        console.log("Score:" + grade + ". Grade: D" + sym);
    } else {
        console.log("Score:" + grade + ". Grade: F");
    }

}

//tests
letterGrade(90);
letterGrade(0);
letterGrade(91);
letterGrade(88);
letterGrade(94);
letterGrade(100);
