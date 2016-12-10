function drawLeftStars(num) {
    console.log("*".repeat(num));
}



function drawRightStars(num) {
    console.log(" ".repeat(75-num) + "*".repeat(num));

}


function drawCenterStars(num) {

    var leftSide = Math.floor((75 - num) / 2);
    var rightSide = Math.ceil((75 - num) / 2)
    console.log(" ".repeat(leftSide) + "*".repeat(num) + " ".repeat(rightSide));
}

//tests
drawLeftStars(75);
drawRightStars(70);
drawCenterStars(60);
