

function likeWord(element){
    alert('Ninja was liked');  
}

function removeButton(element) {
    element.remove();
}


function changeLoginToLogout(element) {
    element.innerText = (element.innerText == 'Login')?'Logout':'Login';
    //document.getElementById("loginLogout").innerText = "Logout"
}