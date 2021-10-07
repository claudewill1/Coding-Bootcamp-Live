/* Factorial
Write code that will multiply all of the values from 1-12 onto some variable product and at the end console.log 
the result 1 * 2 * 3 * ... * 10 * 11 * 12. We should get back 479001600 at the end. */

function Factorial(number) {
    // using recursion
    if(number === 1) return number;
    return number * Factorial(number - 1);
}

// using a for loop the Big O would be O(n!) which is slow
// using recursion the Big O would be O(n) which is the next to fastest outside of O(log n) - second fastest and O(1) fastest


console.log(Factorial(12))