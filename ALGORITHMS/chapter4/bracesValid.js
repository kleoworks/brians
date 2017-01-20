// given string determine if sequence of parens, braces, and brackets are valid


function bracesValid(str) {

    var open_brace = {
        '(': 'parens',
        '[': 'bracket',
        '{': 'curly',
        'parens': 0,
        'bracket': 0,
        'curly': 0
    }

    var close_brace = {
        ')': 'parens',
        ']': 'bracket',
        '}': 'curly',
        'parens': 0,
        'bracket': 0,
        'curly': 0
    }


    for (var i = 0; i < str.length; i++) {

        if (str[i] in open_brace) {

            open_brace[open_brace[str[i]]] += 1;

        } else if (str[i] in close_brace) {

            close_brace[close_brace[str[i]]] += 1;

            if (close_brace[close_brace[str[i]]] > open_brace[close_brace[str[i]]]) {
                return false;
            }

        }

    }

    if (open_brace['parens'] == close_brace['parens'] && open_brace['bracket'] == close_brace['bracket'] && open_brace['curly'] == close_brace['curly']) {

        return true

    } else {
        return false;
    }

}


console.log(bracesValid('{}()[]'));
console.log(bracesValid('}{}()[]'));
console.log(bracesValid('D(i{a}l[ t]o)n{e'))
