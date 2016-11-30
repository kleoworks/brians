for (var i = -300; i < 0; i++) {
    if (i === -3 || i === -6) {
        continue;
    }
    if (i % 3 === 0) {
        console.log(i);
    }
}
