function sweatshirtPricing(num) {

    var teeCost = 20;

    if (num >= 4) {
        teeCost = Math.ceil((teeCost * num) * 0.65); // 35% disc
    } else if (num == 3) {
        teeCost = Math.ceil((teeCost * num) * 0.81); // 19% disc
    } else if (num == 2) {
        teeCost = Math.ceil((teeCost * num) * 0.91); // 9% disc
    } else {
        teeCost = teeCost * num;
    }
    return teeCost;
}

//tests
console.log(sweatshirtPricing(1));
console.log(sweatshirtPricing(2));
console.log(sweatshirtPricing(3));
console.log(sweatshirtPricing(4));
console.log(sweatshirtPricing(10));
