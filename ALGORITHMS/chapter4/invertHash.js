// given an associate array i.e hash... invert the keys and values return new object

function invertHash(obj) {

    for (key in obj) {

        temp = obj[key];
        obj[temp] = key;
        delete obj[key];

    }

    return obj;
    
}

// test
my_obj = {

    'name': 'Zaphod',
    'charm': 'high',
    'morals': 'dicey'
}
console.log(invertHash(my_obj));
