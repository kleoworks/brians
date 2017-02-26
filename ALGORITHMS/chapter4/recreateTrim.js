// remove white space(spaces, tabs, newlines) from both sized of string, and return new string.
// " \n hello goodbye \t" returns "hello goodbye"

function recreateTrim(str) {

    left_idx = 0;
    right_idx = str.length-1;
    temp_str = "";


    // check for whitespace starting at front of string
    for (var i = left_idx; i < str.length; i++) {

        if (str[i] == "\t" || str[i] == " " || str[i] == "\n") {

            continue;

        } else {

            left_idx = i;
            break;
        }

    }

    // check for whitespace starting at back of string
    for (var i = right_idx; i >= left_idx; i--) {

        if ( str[i] == "\t" || str[i] == " " || str[i] == "\n") {

            continue;

        } else {

            right_idx = i + 1; // add 1 so that this character's index is included when slicing from left_idx to right_idx
            break;

        }

    }


    // slice string from left_idx up to not including right_idx
    for (var i = left_idx; i < right_idx; i++) {

        temp_str += str[i];

    }


    return temp_str;

}

// tests
crazy_str = "\n     \n" +
    "                           " +
    "     \n" +
    "C r azzzzyyyyy         " +
    " STRING           " +
    "\n \n \n                              \t"


console.log(recreateTrim("      brian    1    "))
console.log(recreateTrim(crazy_str));
console.log(recreateTrim("brian s"))
