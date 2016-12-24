
// Second: create distFromHome(). Assuming she moves diagonally, return her distance from home.

var claire = {
    "x": 0,
    "y": 0
}

function reset() {
    claire.x = 0;
    claire.y = 0;
}

function moveBy(xOffset, yOffset) {

    claire.x += xOffset;
    claire.y += yOffset;

}

function xLocation() {
    return claire.x;
}

function yLocation() {
    return claire.y;
}


function distFromHome() {
    return (Math.sqrt(Math.pow((xLocation() - 0),2) + Math.pow((yLocation() - 0),2)));
}


//test
reset();
moveBy(1,-2);
moveBy(3,1);
console.log(xLocation());
console.log(yLocation());
console.log(distFromHome());
