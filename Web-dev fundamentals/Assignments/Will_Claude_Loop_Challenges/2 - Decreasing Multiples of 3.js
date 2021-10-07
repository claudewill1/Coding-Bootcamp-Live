// using a loop, print all of the values that are evenly divisible from 3 from 100 to 0.

function DecreasingMultiplesOfThree() {
    for(let i = 100; i >= 0; i--) {
        if(i % 3 === 0) {
            console.log(i);
        }
    }
}

DecreasingMultiplesOfThree()