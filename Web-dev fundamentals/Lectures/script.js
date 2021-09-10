function showMessage() {
    alert(`It's a-me, Mario!`)
}

function showInnerText(element) {
    alert(element.innerText)
}

function removeElement(element) {
    element.remove()
}

let greenText = document.getElementById("greenText")
function makeDiffElementVanish() {
    greenText.remove();
}
let numClaps = 0
let count = document.getElementById("count")
function clapMore() {
    numClaps++
    count.innerText = numClaps
}