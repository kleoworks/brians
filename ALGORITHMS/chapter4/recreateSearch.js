// search string for given val (another string).. return index position of the first match found or -1 if not found

function recreateSearch(str, val) {

    str = (str !== "") ? str : undefined;
    val = (val !== "") ? val : undefined;

    if (str == undefined || val == undefined) {

        return 'must enter a string and value to search.... recreateSearch(string, value)'
    }

    for (var i = 0; i < str.length; i++) {

        if (i + val.length > str.length)   {

            return -1;

        } else {

            if (str[i] == val[0]) {

                start_idx = i;
                loop_idx = i;

                // check if val is in string for remaining length of val, starting with next character! j=1
                for (var j = 1; j < val.length; j++) {

                    loop_idx++;

                    if (str[loop_idx] !== val[j]) {

                        // word not found! re-enter outside loop
                        break;

                    } else if (j == val.length - 1) {

                        // word found!  return index
                        return start_idx;

                    }

                }

            }

        }

    }

}

// tests
console.log(recreateSearch('brian was here', ""));
console.log(recreateSearch());
console.log(recreateSearch('brian was here', "here"));
console.log(recreateSearch('brian was here', "was"));
console.log(recreateSearch('brian was here', "er"));
