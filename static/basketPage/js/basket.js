const counts = document.querySelector("#basketcount")
const bin_button = document.querySelectorAll(".bin_button")   

function updatecount(){
    var count = 0
    if (document.cookie != ""){
        var products = document.cookie.split("=")[1].split(" ")
        for (var i = 0; i < products.length; i++){
            if (products[i] != ""){
                count++
            }
        }
        var infoOrder = document.querySelector(".info_order h3")
        console.log(infoOrder)
        if (infoOrder != null){
            infoOrder.innerText = count + " товари на суму"
        } else{
            document.querySelector(".info_order_none h3").innerText = count + " товари на суму"
        }
        
    }
    counts.textContent = count
    counts.style.display = count > 0 ? "flex":"none"

}

if (document.cookie == ""){
    counts.style.display = "None"
}else{
    updatecount()
}

//-
document.querySelectorAll(".minus_count").forEach(function(button){
    button.addEventListener("click", function(event){
        event.preventDefault()

        var get_id_button = this.id

        var products = document.cookie.split("=")[1].split(" ")
        var index = products.indexOf(get_id_button)
        if (index > -1){
            products.splice(index, 1)
        }
        document.cookie = `product = ${products.join(" ")}; path = /`
        if (products.indexOf(get_id_button) == -1){
            button.closest(".product_content").remove()
        }


        button.closest(".product_text").querySelector(".count_in_basket").innerText = products.filter(id => id == get_id_button).length
        updatecount()
        })
})

//+
document.querySelectorAll(".plus_count").forEach(function(button){
    button.addEventListener("click", function(event){
        event.preventDefault()

        var get_id_button = this.id

        var products = document.cookie.split("=")[1]
        document.cookie = `product = ${products} ${get_id_button}; path = /`

        button.closest(".product_text").querySelector(".count_in_basket").innerText = (products.match(new RegExp(get_id_button, 'g' ))|| []).length +1

        updatecount()
        })
})
document.querySelectorAll(".product_text").forEach(function(product){
    var minusCount = product.querySelector(".minus_count")
    if (minusCount != null){
        var productId = minusCount.id
    }else{
        var productId = product.querySelector(".minus_count_none").id
    }
    
    var products = document.cookie.split('=')[1]
    var countBasket = product.querySelector(".count_in_basket")
    if(countBasket != null){
        countBasket.innerText =  (products.match(new RegExp(productId, 'g' ))|| []).length;
    }else{
        product.querySelector(".count_in_basket_fixed").innerText =  (products.match(new RegExp(productId, 'g' ))|| []).length;
    }
    
});


function update_discount_and_total(){
        var totalSum = 0
        var totalDiscount = 0
        var count = null
        var productId = null
        document.querySelectorAll('.product_content').forEach(function(product){
            var price = parseFloat(product.querySelector('.product_price').innerText)
            var countData = product.querySelector('.count_in_basket')
            if (countData != null){
                count = parseInt(countData.innerText)
            } else{
                count = parseInt(product.querySelector('.count_in_basket_fixed').innerText)
            }
            var minusCountData = product.querySelector(".minus_count")
            if(minusCountData != null){
                var productId = minusCountData.id
            }else{
                var productId = product.querySelector(".minus_count_none").id
            }
            

            var discount = document.querySelector("#discount-" + productId).value
            var productCount = count * price
            var discount_sum = Math.round(productCount * discount / 100) // скидка для каждого товара
            totalSum += productCount
            totalDiscount += discount_sum // суммируем скидки
        })
        var totalSumDiscount = totalSum - totalDiscount // общая сумма со скидкой
        var infoOrder = document.querySelector(".info_order h2")
        var saleData = document.querySelector(".sale h2")
        var totalSumData = document.querySelector(".total_sum h2")
        console.log(infoOrder)
        if (infoOrder != null){
            document.querySelector(".info_order h2").innerText = totalSum + "грн"
        }else{
            document.querySelector(".info_order_none h2").innerText = totalSum + "грн"
        }
        if(saleData != null){
            saleData.innerText = totalDiscount + "грн"
        }else{
            document.querySelector(".sale_none h2").innerText = totalDiscount + "грн"
        }        
        if(totalSumData != null){
            totalSumData.innerText = totalSumDiscount + "грн" 
        }else{
            document.querySelector(".total_sum_none h2").innerText = totalSumDiscount + "грн" 
        }

        
        
}
    
update_discount_and_total()

document.querySelectorAll(".minus_count, .plus_count").forEach(function(button){
    button.addEventListener("click", function(event){
        update_discount_and_total()
    })
})

bin_button.forEach(function(button){
    button.addEventListener("click", function(event){
        event.preventDefault()
        var product_id = this.closest(".product_content").querySelector(".minus_count").id 

        var product = document.cookie.split("=")[1].split(" ")
        product = product.filter(id => id != product_id)
        document.cookie = `product = ${product.join(" ")}; path = /`
        this.closest(".product_content").remove()
        updatecount()
        update_discount_and_total()
    })
})

var formWindow = document.querySelector(".make_order")
var orderButton = document.querySelector(".order")
if(orderButton != null){
    orderButton.addEventListener("click", function(event){
        event.preventDefault()
        console.log('нажатие')
        formWindow.parentElement.style.display = "flex"
        
    })
}else{
    console.log('відмовити?')
}


