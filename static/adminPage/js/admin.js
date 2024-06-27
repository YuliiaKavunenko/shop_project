document.querySelectorAll(".edit").forEach(function(button){

    button.addEventListener("click", function(event){

        event.preventDefault()
        var id_parts = this.id.split('-')
        console.log(id_parts)
        var field = id_parts[1]
        console.log(field)
        var product_id = id_parts[2]

        if(field == "memory"){
            var buttonIndex = this.id.split('-')[3]
            document.querySelector("input[name = index_button_" + product_id + "]").value = buttonIndex


            document.querySelector("#modal-" + field + "-" + product_id).parentElement.style.display = "block"
            document.querySelector("#modal-" + field + "-" + product_id).style.display = "block"
            document.querySelector("#save-" + field + "-" + product_id).style.display = "block"
            document.querySelector("#input-" + field + "-" + product_id).value = document.querySelector("#memory-" + buttonIndex + "-" + product_id).innerText
            document.querySelector("#input-" + field + "-" + product_id).style.display= "block"

            
        }else{
            document.querySelector("#modal-" + field + "-" + product_id).parentElement.style.display = "block"
            document.querySelector("#modal-" + field + "-" + product_id).style.display = "block"
            document.querySelector("#save-" + field + "-" + product_id).style.display = "block"
            document.querySelector("#input-" + field + "-" + product_id).style.display= "block"        
        }


    })
})

let add_button = document.querySelector(".add_button")
add_button.addEventListener("click", function(event){
    event.preventDefault()
    let add_modal = document.querySelector(".modal1")
    add_modal.style.display = "block"
    add_modal.parentElement.style.display = "block"
})


document.querySelectorAll('.delete-dutton').forEach(function(button){
    button.addEventListener('click',function(event){
        event.preventDefault()

        var id = this.id.split('-')[2]

        this.closest(".product").remove()
    })
})


