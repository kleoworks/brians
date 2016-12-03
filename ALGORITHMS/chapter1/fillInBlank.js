// ask user's name
// ask some questions, use prompt() and compare to answer expected
// print statistics: user name, number of questions and correct

var quiz = [["What's 2*2?", 4],["What color is your favorite dinosaur?", "purple"]];

var user = prompt("Hello there.  What's your name?");

var count = 0;

if (user != "") {
    var answer = prompt("Hey " + user + "! You ready for a quiz? type: y/n");

    if (answer == "y") {

        //question 1
        quiz[0][2] = prompt(quiz[0][0]);
        if (quiz[0][1] !== quiz[0][2]) {
            console.log("seriously!");
        } else {
            console.log("great math!");
            count++;
        }

        //question 2
        quiz[1][2] = prompt(quiz[1][0]);
        if (quiz[1][1] !== quiz[1][2]) {
            console.log("i disagree!")
        } else {
            console.log("wow! mine too!");
            count++
        }

    } else {
        console.log("that was not an acceptable answer.... goodbye!");
    }

    console.log(user + " you got " + count + " correct out of 2!");

}
