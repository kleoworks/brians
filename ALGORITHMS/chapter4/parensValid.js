// function with str input, return boolean whether parens in str are valid
// valid means always open before close
// For Y(3(p)p(3)r)s return true
// For N(0(p)3 return false

function parens_valid(str) {

    var left = 0;
    var right = 0;

    for (var i = 0; i < str.length; i++) {

        if (str[i] == "(") {

            left += 1;

        } else if (str[i] == ")") {

            right += 1;

            if (right > left) {
                return false
            }

        }

    }

    if (left == right) {
        return true;
    } else {
        return false;
    }

}

console.log(parens_valid('Y(3(p)p(3)r)s'));
console.log(parens_valid('N(0(p)3'));
console.log(parens_valid('N(0)t ) 0 (k'));
