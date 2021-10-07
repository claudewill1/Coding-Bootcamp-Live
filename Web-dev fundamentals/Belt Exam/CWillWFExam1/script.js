
/* Show Linux Compatability */
function showSupport() {
    alert("This game is supported by Linux")
}
const stonepunk = document.getElementById("stonepunk");
const cafeNeko = document.getElementById("cafe-neko");
const pixelNijas2 = document.getElementById("pixel-ninjas-2");
const stonepunkImgSrc = "./images/stonepunk.png";
const cafeNekoImgSrc = "./images/cafe-neko.png";
const pixelNinjasSrc = "./images/pixel-ninjas-2.png";
let gameImg = document.getElementById("game");
let left = document.getElementById("chevron-left");
let right = document.getElementById("chevron-right");
let indicatorContainer = document.getElementsByClassName("carousel-indicators");
// get all items with li element inside container
let indicators = document.getElementsByTagName("li");
/* first image will change to second image with this, but third image won't work and the back
portion of the function doesn't work  
Will schedule a code review later */
function changeSlideRight() {
   let current = document.getElementsByClassName("active");
    
    
    var imgs = [stonepunkImgSrc,cafeNekoImgSrc,pixelNinjasSrc]
    let imgx;
    
    current[0].classList.remove("active")
    if(right)
    {     
            for(imgx = 0; imgx < imgs.length; imgx++) {
                if(document.getElementById("game").src === imgs[0]) {
                    document.getElementById("game").src = imgs[imgx]
                } 
                else if (document.getElementById("game").src === imgs[imgx]) {
                    
                    document.getElementById("game").src= imgs[imgx];
                } else {
                    document.getElementById("game").src = imgs[imgx];
                }
                //current[imgx] += 1;
                console.log(imgx);
            }
        
    }    
}

/* active indicator changes, first image will change to second img*/
function changeWithIndicator(e) {
    let current = document.getElementsByClassName("active");
    var imgs = [stonepunkImgSrc,cafeNekoImgSrc,pixelNinjasSrc]
    let imgx;
    current[0].classList.remove("active")
    e.className += "active";
    for(imgx = 0; imgx < imgs.length; imgx++) {
                if(document.getElementById("game").src === imgs[imgx]) {
                    document.getElementById("game").src = imgs[imgx]
                } else if (document.getElementById("game").src === imgs[1]) {
                    
                    document.getElementById("game").src= imgs[imgx];
                } else {
                    
                    document.getElementById("game").src = imgs[imgx];
                }
                
        }
    }
    

let numItems = 0;
let count = document.getElementById("cartCount")
function addToCart() {
    numItems++;
    count.innerText = numItems;
}
