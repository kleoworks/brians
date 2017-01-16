// create function given a string, returns the integer made from the string's digits
// given '0s1a3y5w7h9a2t4?6!8?0', return 1357924680
// 9m

function getDigits(str) {

    new_str = ""

    for (var i = 0; i < str.length; i++) {

        if (parseInt(str[i],10) <= 9 || parseInt(str[i],10) >= 0) {
            new_str += str[i];
        }

    }

    return parseInt(new_str,10);

}

// test
console.log(getDigits('0s1a3y5w7h9a2t4?6!8?0!@#$$%^&*()_+-=[]]>><</\\'));
