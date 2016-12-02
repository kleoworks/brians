function hungry(arr) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("yummy");
            count++;
        }
    }
    if (count === 0) {
        console.log("I'm hungry");
    }

}

//test
hungry([0, 2, "forty", "foods-", "food", "food", 2]); // prints yummy twice
hungry(["eat", "your", "veggies"]); // prints I'm hungry once
