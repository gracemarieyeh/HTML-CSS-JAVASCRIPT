let Toyota = {
    color : "Silver",
    country : "Japan",
    priceArr : [10000, 20000, 30000],
};

let Mercedes = {
    color : "red",
    country : "America",
    priceArr : [40000, 50000, 60000],
};

let carArr = [Toyota, Mercedes];

console.log("The Toyota car is from");
console.log(carArr[0].country);
console.log("It has a price range of");

let i;
for(i = 0; i < 3; ++i) {
    console.log(carArr[0].priceArr[i]);
}

