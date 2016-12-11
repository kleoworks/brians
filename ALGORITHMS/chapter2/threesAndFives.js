// 100 and 4000000
//
// 3 or 5 not both
//


function ThreesFives() {
    var sum = 0;
    for (var i = 100; i <= 4000000; i+=1) {
        if ((i % 3 === 0 || i % 5 === 0) && i % 15 !== 0) {
            sum+=i;
        }
    }
    return sum;
}


function BetterThreesFives(start, end) {
    var sum = 0;
    for (var i = start; i <= end; i+=1) {
        if ((i % 3 === 0 || i % 5 === 0) && i % 15 !== 0) {
            sum+=i;
        }
    }
    return sum;
}


//tests
console.log(ThreesFives());
console.log(BetterThreesFives(10,200));
