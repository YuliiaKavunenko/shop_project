const list_buttons = document.querySelectorAll(".buy_button")
const counts = document.querySelector("#basketcount")

function updatecount(){
    var count = 0
    if (document.cookie != ""){
        var products = document.cookie.split("=")[1].split(" ")
        for (var i = 0; i < products.length; i++){
            if (products[i] != ""){
                count++
            }
        }
    }
    counts.textContent = count
    counts.style.display = count > 0 ? "flex":"none"
}
updatecount()
