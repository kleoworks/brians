// create a function that, given a string, returns all of that string's contents, but without the blanks.
// if given the string " P1     ayTha    tF    u   nkyM   usi     c  ", return PlayThatFunkyMusic
// 12m


function removeBlanks(str) {

    var str_arr = [];

    for (var i = 0; i < str.length; i++) {
        if (str[i] != " " && str[i] != '\t' && str[i] != '\n') {
            str_arr.push(str[i]);
        }
    }

    new_str = str_arr.join("");

    return new_str;

}

// test
str1 = " Pl     ayTha    tF    u   nkyM   usi     c  "
console.log(removeBlanks(str1));
