// split string into an array of substrings, return array
// split on separator .. if "" split every character
// limit optional and indicates number of splits
// no change to existing string

function recreateSplit(str, sep, limit) {

    limit = (limit !== undefined) ? limit : 0;
    temp_str = "";
    temp_arr = [];

    if (limit > 0 ) {

        sep_count = 0;

        for (var i = 0; i < str.length; i++) {

            if (sep == "") {

                for (var i = 0; i < str.length; i++) {

                    if (sep_count < limit) {
                        temp_arr.push(str[i]);
                        sep_count++;
                    }

                }

            } else {


                if (str[i] == sep && sep_count < limit) {

                    temp_arr.push(temp_str);
                    temp_str = "";
                    sep_count++;

                } else {

                    temp_str += str[i];

                    if (i == str.length - 1 && temp_str !== "" && sep_count < limit) {

                        temp_arr.push(temp_str);
                        sep_count++;

                    }

                }

            }

        }

    } else {

        if (sep == "") {

            for (var i = 0; i < str.length; i++) {

                temp_arr.push(str[i]);

            }

        } else {

            for (var i = 0; i < str.length; i++) {

                if (str[i] == sep) {

                    temp_arr.push(temp_str);
                    temp_str = "";

                } else {

                    temp_str += str[i];

                    if (i == str.length - 1 && temp_str !== "") {

                        temp_arr.push(temp_str);

                    }

                }

            }

        }

    }

    return temp_arr;

}


// tests
console.log(recreateSplit('brian', ""));
console.log(recreateSplit('brian was here', " "));
console.log(recreateSplit('brian was here', " ", 2));
console.log(recreateSplit('brian was here', "", 5));
