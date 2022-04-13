function redirect(){
    let url = "http://127.0.0.1:5000/edit/2"
    window.location.href = url
}
function redirect2(){
    let url = "http://127.0.0.1:5000/view/2"
    window.location.href = url
}
function saveEdits() {

//get the editable element/c
    console.log("in save edits ")
    let title = $.trim($("#title_to_save").val())
    let no_error = true
    console.log("Manesdaa", title)

    if (no_error) {
        let new_data = {
            "title": "Manresa"
        }
        save_title(new_data)
    }
}

function save_title (new_data){

    let data_to_save = {"new_data": new_data}
    $.ajax({
        type: "POST",
        url: "edit/<id>",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_data),
	    success: function(data, text){
			// display_sales_list(data["sales"])
            redirect2()

	    },

    });


}

  $( function() {
    $( "#dialog" ).dialog({
      autoOpen: false,
      show: {
        effect: "blind",
        duration: 1000
      },
      hide: {
        effect: "explode",
        duration: 1000
      },
        buttons: {
        "Discard all changes": function() {
          $( this ).dialog( "close" );
          redirect()
        },
        Cancel: function() {
          $( this ).dialog( "close" );
        }
      }
    });

    $( "#opener" ).on( "click", function() {
      $( "#dialog" ).dialog( "open" );
    });
  } );

$(document).ready(function(){



    $("#delete_button").click(function (e) {
         console.log("view result button clicked")
         e.preventDefault()

         redirect()




        })
    $("#save_button").click(function (e) {
         console.log("view result button clicked")
         e.preventDefault()

         saveEdits()
         redirect2()




        })


})