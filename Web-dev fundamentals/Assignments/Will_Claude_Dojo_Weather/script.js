

function changeTemp() {
    let tempType = document.getElementById("celciusFahrenheit").value;
    let tempH = document.querySelectorAll(".tempH");
    let tempL = document.querySelectorAll(".tempL");
    tempH.forEach(function (h) {

        if(tempType === "f") {
            h.innerHTML = parseFloat((parseInt(h.innerHTML) * 9 / 5) + 32).toFixed(1);
        } else if (tempType === "c") {
            h.innerHTML = parseFloat((parseInt(h.innerHTML) - 32) * 5 / 9).toFixed(1);
        }

    });
    tempL.forEach(function (l) {

        if(tempType === "f") {
            l.innerHTML = parseFloat((parseInt(l.innerHTML) * 9 / 5) + 32).toFixed(1);
        } else if (tempType === "c") {
            l.innerHTML = parseFloat((parseInt(l.innerHTML) - 32) * 5 / 9).toFixed(1);
        }

    });
}

function loading() {
    alert("Loading weather report...");
}

function removeDiv() {
    document.getElementById("cookieConsent").remove();

}