//shortcut sum of odd integers -300,000 to 300,000
console.log(0);

//long way
var sum = 0;

for (var i = -300000; i <= 300000; i++) {
    if (i % 2 !== 0) {
        sum+=i;
    }
}
console.log(sum);
