
let user1 = document.getElementById("like1").innerText;
let user2= document.getElementById("like2").innerText;
let user3 = document.getElementById("likes3").innerText;
let count;
function addLike() {
    if(e.document.getElementById("btn1")) {
        count = user1;
        count++;
        user1.innerText = count;
    } else if (e.document.getElementById("btn2")) {
        count = user2;
        count++
        user2.innerText = count;
    } else if (e.document.getElementById("btn3")) {
        count = user3;
        count++;
        user3.innerText = count;
    }
}
