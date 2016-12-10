function drawLeftChars(num, char) {
    console.log(char.repeat(num));
}



function drawRightChars(num, char) {
    console.log(" ".repeat(75-num) + char.repeat(num));

}


function drawCenterChar(num, char) {

    var leftSide = Math.floor((75 - num) / 2);
    var rightSide = Math.ceil((75 - num) / 2)
    console.log(" ".repeat(leftSide) + char.repeat(num) + " ".repeat(rightSide));
}

//tests
drawLeftChars(75,"$");
drawRightChars(70,"$");
drawCenterChar(60,"$");
