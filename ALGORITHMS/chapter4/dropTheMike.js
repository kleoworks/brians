// accept a string, remove leading and trailing white space (beginning and end only),
// capitalize first letter of every word
// return the string
//
// if Mike is contained anywhere returned 'stunned silence'

function dropTheMike(str) {

    temp_str = ""
    temp_arr = []

    for (var i = 0; i < str.length; i++) {

        if (str[i] == " ") {

            if (temp_str == "") {

                continue;

            } else {

                if (temp_str == 'Mike') {

                    return 'stunned silence';

                } else {

                    temp_arr.push(temp_str);
                    temp_str = "";
                    continue;
                }
            }

        } else {

            temp_str += str[i];

        }

    }


    for (var i = 0; i < temp_arr.length; i++) {

        temp_str = "";

        for (var j = 0; j < temp_arr[i].length; j++) {

            if (j !== 0) {

                temp_str += temp_arr[i][j];

            } else {

                temp_str += temp_arr[i][j].toUpperCase();

            }

        }

        temp_arr[i] = temp_str;

    }

    return temp_arr.join(" ");

}


// test
console.log(dropTheMike(' this is a test!   1!'));
console.log(dropTheMike(' this is a test!  Mike 1!'));
console.log(dropTheMike('Mike this is a test!  Mike 1!'));
console.log(dropTheMike('     this is a test!  Mi ke mi ke  dddkkd Mik 1!'));
