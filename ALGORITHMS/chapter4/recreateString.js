function recreateString() {

    temp_str = "";

    for (var i = 0; i < arguments.length; i++) {

        temp_str += arguments[i];

    }

    return temp_str;
}

console.log(recreateString("I want", " ", "to ", "code!"));
