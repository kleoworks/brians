function generateCoinChange(cents) {

    var change = cents;

    var quarters = Math.floor(change/25);
    change-=quarters * 25;

    var dimes = Math.floor(change/10);
    change-=dimes * 10;

    var nickels = Math.floor(change/5);
    change-=nickels * 5;

    var pennies = change;

    console.log(cents + " cents can be represeted by:");
    console.log("quarters: " + quarters);
    console.log("dimes: " + dimes);
    console.log("nickels: " + nickels);
    console.log("pennies: " + pennies);
}

//
function generateCoinChangeExtra(coins){
    console.log(coins + " cents can be represented by:");
    console.log("silver dollars: " + Math.floor(coins/100));
    coins-=Math.floor(coins/100)*100;
    console.log("half dollars: " + Math.floor(coins/50));
    coins-=Math.floor(coins/50)*50;
    console.log("quarters: " + Math.floor(coins/25));
    coins-=Math.floor(coins/25)*25;
    console.log("dimes: " + Math.floor(coins/10));
    coins-=Math.floor(coins/10)*10;
    console.log("nickels: " + Math.floor(coins/5));
    coins-=Math.floor(coins/5)*5;
    console.log("pennies: " + coins);
}




//tests
generateCoinChange(94);
generateCoinChangeExtra(237);
