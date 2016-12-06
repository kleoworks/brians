
// 30 days
var penny = 0;

for (var i = 1; i <= 30; i+=1) {
    if (penny !== 0) {
        penny*=2;
    } else {
        // penny for the first day!
        penny+=.01;
    }
}

console.log("After 30 days: $" + penny);


// days to make 10,000
var penny = 0;
var days = 0;

while (penny <= 10000) {
    if (penny !== 0) {
        penny*=2;
    } else {
        penny+=.01;
    }
    days+=1;
}

console.log("It will take " + days + " days to make 10k");
console.log("$" + penny);



// days to make 1 billion
var penny = 0;
var days = 0;

while (penny <= 1000000000) {
    if (penny !== 0) {
        penny*=2;
    } else {
        penny+=.01;
    }
    days+=1;
}

console.log("It will take " + days + " days to make 1 billion");
console.log("$" + penny);


// days to make infinity
var penny = 0;
var days = 0;

while (penny < Infinity) {
    if (penny !== 0) {
        penny*=2;
    } else {
        penny+=.01;
    }
    days+=1;
}

console.log("It will take " + (days) + " days to make INFINITY");
console.log("$" + penny);
