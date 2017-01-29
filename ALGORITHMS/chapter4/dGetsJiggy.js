// given name as string, remove first letter from name, capitalize the new name and add the removed letter to the end of the greeting....  for 'Dylan' return 'Ylan to the D!''

function getJiggy(name) {

    var greeting_start = "";
    var greeting_end = "";

    if (name.length > 2) {

        for (var i = 0; i < name.length; i++) {

            if (i > 1) {

                greeting_start+=name[i];

            } else if (i == 0) {

                greeting_end += name[i];

            } else if (i == 1) {

                greeting_start+=name[i].toUpperCase();

            }

        }

    } else {

        return name;

    }

    greeting_start += " to the ";
    greeting_end += "!";

    return greeting_start + greeting_end;
}


// test
console.log(getJiggy('Dylan'));
console.log(getJiggy('BS'));
console.log(getJiggy('Brian'));
