// given string, return string with characters reversed... do not use reverse()

function stringReverse(str) {

    new_str = "";

    for (var i = str.length -1; i >= 0; i--) {

        new_str += str[i];

    }

    return new_str;

}

//test
console.log(stringReverse('creature'));
