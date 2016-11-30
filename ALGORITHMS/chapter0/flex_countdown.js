function flexCount(lowNum, highNum, mult) {
    for (var i = highNum; i > lowNum; i-=mult) {
        console.log(i);
    }
}

//tests
console.log("2,9,3");
flexCount(2,9,3);
console.log("2,200,50");
flexCount(2,200,50);
