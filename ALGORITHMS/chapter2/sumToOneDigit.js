function sumToOne(num) {

    var str = num.toString();

    if (num == 0 || num == 1) {
        return num;
    }

    while (str.length > 1) {

        var sum = 0;

        for (var i = 0; i < str.length; i+=1) {
            sum+= parseInt(str[i],10);
        }

        str = sum.toString();
    }

    return sum;
}

//tests
console.log(sumToOne(928));
console.log(sumToOne(394));
console.log(sumToOne(1));
