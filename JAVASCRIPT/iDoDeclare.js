var num1 = 10;
var num2 = 10.5;
var num3 = -12;
var num4 = 5000;

var str1 = "hello";
var str2 = "yo!";
var str3 = "bye!";

var bool1 = true;
var bool2 = false;

var myVar;

var index = ["","First", "Second", "Third", "Forth"];

// print numbers
for (var i = 1; i <= 4; i++) {
    console.log("The " + index[0+i] + " Number: " +  eval("num" + i));

}

// print strings
for (var i = 1; i <= 3; i++) {
    console.log("The " + index[0+i] + " String: " +  eval("str" + i));
}

// print booleans
for (var i = 1; i <= 2; i++) {
    console.log("The " + index[0+i] + " Boolean: " +  eval("bool" + i));
}


// print undefined
console.log("The undefined variable: " + myVar);
