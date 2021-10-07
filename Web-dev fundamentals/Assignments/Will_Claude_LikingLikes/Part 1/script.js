let likes = document.querySelector("#like");
let count = document.getElementById('like').innerText;
function addLike() {

    count++;
    likes.innerText = count;
}