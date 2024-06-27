var modal = document.getElementById("modal_window");
var button = document.getElementById("auth_button");
var span = document.getElementById("close");
// var link = document.getElementById("authorization");

span.onclick = function(){
    modal.style.display = "none";
    document.getElementById("auth_content").submit();
}

button.onclick = function(event){
    modal.style.display = "block";
    event.preventDefault();
}
window.onclick = function(event){
    if (event.target == modal){
        modal.style.display = "none";
        document.getElementById("auth_content").submit();
    }
}
    
