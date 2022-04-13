function redirect(){
    let url = "http://127.0.0.1:5000/edit/2"
    window.location.href = url
}
$(document).ready(function(){



    $("#edit_button").click(function (e) {
         console.log("view result button clicked")
         e.preventDefault()
         redirect()




        })


})