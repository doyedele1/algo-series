var kidsWithCandies = function(candies, extraCandies) {
    let maxCandy = Math.max(...candies);
    console.log(maxCandy);

    outputArr = [];

    for(let i = 0; i < candies.length; i++) {
    
        let addedCandies = candies[i] + extraCandies;
    
        if(addedCandies >= maxCandy) {
            outputArr.push(true);
        }
        else {
            outputArr.push(false);
        }
    }

    return outputArr
};

console.log(kidsWithCandies([2,3,5,1,3], 3));
console.log(kidsWithCandies([4,2,1,1,2], 1));
console.log(kidsWithCandies([12,1,2], 10));

