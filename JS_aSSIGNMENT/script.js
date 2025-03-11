const image = document.getElementById("image")




const resizeSmall = document.querySelector(".small")

const resizeMedium = document.querySelector(".medium")

const resizeLarge = document.querySelector(".large")

const header = document.querySelector(".heading")


header.innerHTML = "Donald J Trump"

resizeSmall.addEventListener("click", () => {
   image.width = 50;   
})

resizeMedium.addEventListener("click", () => {
    image.width = 300;   
 })

 resizeLarge.addEventListener("click", () => {
    image.width = 400;   
 })



