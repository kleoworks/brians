// function, given string, returns string's acronym (first letters only, capitalized)
// given ' there's no free lunch - gotta pay yer way. ', return 'TNFL-GPYW'
// given 'Live from New York, it's Saturday Night!', return 'LFNYISN'

// 5m


function acronym(str) {

    str_arr = str.split(' ');

    new_str = ""

    for (var i = 0; i < str_arr.length; i++) {

        new_str += str_arr[i][0];

    }

    return new_str.toUpperCase();

}

console.log(acronym("there's no free lunch - gott pay yer way."));
console.log(acronym("Live from New York, it's Saturday Night!"));
