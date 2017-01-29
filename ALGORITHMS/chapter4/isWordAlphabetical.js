// given string return if all letters are in a-z order


function isAlphabetical(str) {

    var letters = 'abcdefghijklmnopqrstuvwxyz'
    var min_idx = 0

    for (var i = 0; i < str.length; i++) {

        for (var j = 0; j < letters.length; j++) {

            if (letters[j] == str[i]) {
                letter_idx = j
                break;
            }

        }

        if (letter_idx >= min_idx) {

            min_idx = letter_idx;

        } else {

            return false;

        }

    }

    return true;

}


// tests
console.log(isAlphabetical('brian'));
console.log(isAlphabetical('abcdefg'));
console.log(isAlphabetical('adfyz'));
console.log(isAlphabetical('adfyaz'));
