// return number of values/keys in object

function numValues(obj) {

    var count = 0;

    for (key in obj) {

        count++;

    }

    return count;

}


// test

my_obj = {

    'band': "Travis Shredd & the Good Ol' Homeboys",
    'style': "Country/Metal/Rap",
    'album': "668: The Neighbor of the Beast"

}

console.log(numValues(my_obj));
