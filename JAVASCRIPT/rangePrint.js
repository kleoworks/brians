function printRange(start, end, skip) {

    // set start, end, skip or set defaults if user does not supply all arguments
    if (end == null) {
        end = start;
        start = 0;
    }

    if (skip == null) {
        skip = 1;
    }

    // print ranges
    if (start < end) {
        for (var i = start; i < end; i+=skip) {
            console.log(i);
        }
    } else if (start > end) {
        for (var i = start; i > end; i-=skip){
            console.log(i);
        }
    }

}

printRange(4,8);
printRange(4);
printRange(-4, 10);
printRange(-1);
