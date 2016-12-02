//given two numbers, return array of length num1 with each value num2.  Print "Jinx!" if they are the same

function thisLengthThatValue(num1, num2) {

    var arr = [];

    if (num1 === num2){
        console.log("Jinx!");
    }
    else {
        for (var i = 0; i < num1; i++) {
            arr.push(num2);
        }
        return arr;
    }

}

//tests
var test1 = thisLengthThatValue(4,5);
var test2 = thisLengthThatValue(5,4);
var test3 = thisLengthThatValue(4,4);
var test4 = thisLengthThatValue(3,3);

console.log(test1); // should print [5,5,5,5]
console.log(test2); // should print [4,4,4,4,4]
console.log(test3); // should print Jinx!
console.log(test4); // should print Jinx!
