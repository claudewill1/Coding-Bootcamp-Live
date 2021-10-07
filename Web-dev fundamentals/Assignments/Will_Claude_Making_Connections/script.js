let username = document.getElementById("userName");
function changeName() {
    username.innerText = prompt("Enter a new name: ");
}

let userRequest1 = document.getElementById("request1");
let userRequest2 = document.getElementById("request2");
let requestCount = document.getElementById("requests");
let connectCount = document.getElementById("count");
let currentCount = parseInt(connectCount.innerText);
console.log(currentCount)
function acceptRequest() {
    
    if (userRequest1) {
        userRequest1.remove();
        requestCount.innerText -= 1;
        connectCount.innerText = currentCount += 1;
    } 
}

function acceptRequest2() {
    
    if (userRequest2) {
        userRequest2.remove();
        requestCount.innerText -= 1;
        connectCount.innerText = currentCount += 1;
    }
}

function rejectRequest() {
    if(userRequest1) {
        userRequest1.remove();
        requestCount.innerText -= 1;
    } 
}

function rejectRequest2() {
    if (userRequest2) {
        userRequest2.remove();
        requestCount.innerText -= 1;
    }
}