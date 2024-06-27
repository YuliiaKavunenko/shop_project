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

for (let i = 0; i < list_buttons.length; i++){
    let button = list_buttons[i] 
    button.addEventListener(
        'click',
        function(event){
            event.preventDefault()
            if (document.cookie == ''){
                document.cookie = `product = ${button.id}; path = /`
            }else{
                let productId = document.cookie.split('=')[1]
                document.cookie = `product = ${productId} ${button.id}; path = /`
            }
            updatecount()
        }
    )
}

var products = document.querySelectorAll(".content")
products.forEach(function(product){
    var buttons = product.querySelectorAll(".КНОПКИ button")
    buttons.forEach(function(button){
        button.addEventListener("click", function(event){
            event.preventDefault()
            buttons.forEach(function(one_button){
                one_button.style.backgroundColor = "white"
            })
            this.style.backgroundColor = "#EFCB4A"
        })
    })
})
updatecount()
