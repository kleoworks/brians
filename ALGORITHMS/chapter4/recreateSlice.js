function recreateSlice(str, idx1, idx2) {

    temp_str = "";

    if (Math.abs(idx1) > str.length || Math.abs(idx2) > str.length) {

        return 'index values can not be larger than string length';
    }

    // positive indices only
    if (idx1 >= 0 && idx2 > idx1) {

        for (var i = idx1; i < idx2; i++) {

            temp_str += str[i];

        }

        return temp_str;

    }

    // positive index1, negative index2
    if (idx1 >= 0 && idx2 < 0) {

        idx2 = str.length + idx2;

        if (idx2 < idx1) {

            return 'invalid indices given';

        } else {

            for (var i = idx1; i < idx2; i++) {

                temp_str += str[i];
            }

            return temp_str;

        }

    }

        // negative index1, postive index2
        if (idx1 < 0 && idx2 >= 0) {

            idx1 = str.length + idx1;

            if (idx2 == 0) {

                idx2 = str.length;

            }

            if (idx2 < idx1) {

                return 'invalid indices given';

            } else {

                for (var i = idx1; i < idx2; i++) {

                    temp_str += str[i];
                }

                return temp_str;

            }

        }



    // negative index both values:
    if (idx1 < 0 && idx2 < 0) {

        idx1 = str.length + idx1;
        idx2 = str.length + idx2;

        if (idx2 < idx1) {

            return 'invalid indices given'
        }

        else {
            for (var i = idx1; i < idx2; i++) {

                temp_str += str[i];
            }

            return temp_str;

        }

    }


}




// tests

console.log(recreateSlice('brian', 1, 4));
console.log(recreateSlice('brian', 1, -1));
console.log(recreateSlice('brian', -3, -1));
console.log(recreateSlice('brian', -4, 4));
console.log(recreateSlice('brian', -4, 0));
