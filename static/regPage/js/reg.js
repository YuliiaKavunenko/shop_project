var modal = document.getElementById("firstModal");
var button = document.getElementById("sendbutton");
var span = document.getElementById("linkreg");

button.onclick = function(event){
    event.preventDefault();
    modal.style.display = "block";
}

window.onclick = function(event){
    if(event.target == modal){
        modal.style.display = "none";
        document.getElementById("reg_content").submit();
    }
}
span.onclick = function(event){

    modal.style.display = "block";
    document.getElementById("reg_content").submit();
    window.location.href = "/authorization/";
}