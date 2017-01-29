// takes a string and returns boolean if strict palindrome
// do not ignore spaces, punctuation or capitalization

function strictPalindrom(str) {

    str_reverse = "";

    for (var i = str.length-1; i >= 0; i--) {

        str_reverse+= str[i];

    }

    return str == str_reverse;


}

// test
console.log(strictPalindrom('a x a'));
console.log(strictPalindrom('racecar'));
console.log(strictPalindrom('Dud'));
console.log(strictPalindrom('oho!'));
