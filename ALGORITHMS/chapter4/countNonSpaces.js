// accept string and return number of non-space chars found in string.
// given "Honey pie, you are driving me crazy", return 29 (not 35)
// 3m

function countNonSpaces(str) {

    str_arr = str.split(' ');
    str_cat = str_arr.join("");

    return str_cat.length;

}

console.log(countNonSpaces('Honey pie, you are driving me crazy'));
