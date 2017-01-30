// given array of words, return the largest suffix common to all words or "" if none
// ['deforestation', 'citation', 'conviction', 'incarceration'] return 'tion'

function commonSuffix(arr) {
    // loop through each word in array
    // compare last letter of each word to the last letter of the first indexed word
    // if letters all match, then add that letter to the the suffix string and re-enter forloop checking the next to last letter, and so on, and so on, until either no match found or no more letters can be compared because loop has reached shortest word length
    // function returns the value of suffix, "" if no matching characters found, or the the matched characters in REVERSE order

    // set up suffix string
    var suffix = "";

    var i = 1;
    while (true) {

        var letter = arr[0][arr[0].length - i];

        for (var j = 1; j < arr.length; j++) {

            if ((arr[j][arr[j].length-i] != letter) || (arr[j].length - i < 0 )) {

                return reverseString(suffix);

            }

        }

        suffix += letter;
        i += 1;

    }

    return reverseString(suffix);

    // function used to return the suffix in reverse
    function reverseString(str) {

        reverse_str = "";
        for (var i = str.length - 1; i >= 0; i--) {
            reverse_str += str[i];
        }
        return reverse_str;
    }

}

//tests
console.log(commonSuffix(['deforestation', 'citation', 'conviction', 'incarceration']));
console.log(commonSuffix(['nice', 'ice', 'baby']));
console.log(commonSuffix(['playing', 'joking', 'riding']));
