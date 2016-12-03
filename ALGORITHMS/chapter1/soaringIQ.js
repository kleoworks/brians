function soaringIQ(x) {
    for (var i = 1; i <= 98; i++) {
        x+= i*.01;
    }
    if (x > 140) {
        console.log("you're a genius!");
    } else if (x > 120) {
        console.log("you're superior but not genius!");
    } else if (x > 110) {
        console.log("you're above average");
    } else {
        console.log("maybe you should spend more time coding!")
    }
    return x;
}

//test
console.log(soaringIQ(101));
console.log(soaringIQ(50));
