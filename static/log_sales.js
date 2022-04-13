


// let sales = [
// 	{
// 		"salesperson": "James D. Halpert",
// 		"client": "Shake Shack",
// 		"reams": 100
// 	},
// 	{
// 		"salesperson": "Stanley Hudson",
// 		"client": "Toast",
// 		"reams": 400
// 	},
// 	{
// 		"salesperson": "Michael G. Scott",
// 		"client": "Computer Science Department",
// 		"reams": 1000
// 	},
// ]
let clients = []

function display_sales_list(sales){
    $("#sales").empty()

    $.each(sales, function(i, sale){
        
        let row = $("<div class = 'row bottom_row_padding'>")
        $("#sales").append(row)

        let col_salesperson = $("<div class = 'col-md-2'>")
        $(col_salesperson).append(sale["salesperson"])
        $(row).append(col_salesperson)

        let col_client = $("<div class = 'col-md-4'>")
        $(col_client).append(sale["client"])
        $(row).append(col_client)

        let col_reams = $("<div class = 'col-md-2'>")
        $(col_reams).append(sale["reams"])
        $(row).append(col_reams)

        let delete_button_div = $("<div class = 'col-md-2'>")
        let delete_button = $("<button class = 'btn btn-warning'>X</button>")
            $(delete_button).click(function(){

                let data_to_delete = {"sale": sale}
                $.ajax({
                    type: "POST",
                    url: "delete_sale",
                    dataType : "json",
                    contentType: "application/json; charset=utf-8",
                    data : JSON.stringify(sale),
                    success: function(data, text){
                        display_sales_list(data["sales"])

                    },

                });
                display_sales_list(sales)
            })

        $(delete_button_div).append(delete_button)
        $(row).append(delete_button_div)
    })
}

// The TA helped me with the code below. He said my code was very close and he made some adjustments that he said were ok for me to include
function save_sale (new_restaurant){


    let data_to_save = {"new_sale": new_restaurant}
    $.ajax({
        type: "POST",
        url: "save_sale",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_restaurant),
	    success: function(data, text){
			// display_sales_list(data["sales"])
            displayButton()


			$("#enter_client").val("")
			$("#enter_reams").val("")
            $("#enter_city").val("")
            $("#enter_price").val("")
            $("#enter_region").val("")
            $("#enter_cuisine").val("")
            $("#enter_wine").val("")
            $("#enter_url").val("")
			$("#enter_client").focus()
	    },

    });


}
function displayButton(){
    $("#see_results").empty()
    $("#see_results").append('<button type="button" id="view_result_button"  onClick="redirect()" class="btn btn-primary btn-lg btn-block">New item successfully created! See it here.</button><br>')
}

function submitSale (){

    $(".warning").empty()

    let client = $.trim( $("#enter_client").val() )
    let reams = $.trim( $("#enter_reams").val() )
    let city = $.trim( $("#enter_city").val() )
    let region = $.trim( $("#enter_region").val() )
    let cuisine = $.trim( $("#enter_cuisine").val() )
    let wine = $.trim( $("#enter_wine").val() )
    let image_url = $.trim( $("#enter_url").val() )
    let wine_with_brackets = "['"+ wine +"']"
    let no_error = true

    if(client == ""){
        $("#blank_warning_div").append('<div class="warning"> Cannot be empty</div>')
        $("#enter_client").val("")
        $("#enter_client").focus()
        no_error = false
    }
    if(reams == ""){
        $("#reams_warning_div").append('<div class="warning"> Cannot be empty</div>')
        $("#enter_reams").val("")
        $("#enter_reams").focus()
        no_error = false
    }


    if(!(reams == "") && !$.isNumeric(reams)){
        $("#reams_warning_div").append('<div class="warning"> Must be a number</div>')
        
        $("#enter_reams").focus()
        no_error = false
    }
    let id = 11

    if(no_error){
        let new_restaurant={
            "id": id,
            "title": client,
            "year": reams,
            "city": city,
            "region": region,
            "cuisine": cuisine,

            "url": image_url,
            "wine": [wine]
        }
        save_sale(new_restaurant)
    }
}

function redirect(){
    let url = "http://127.0.0.1:5000/view/11"
    window.location.href = url
}
$(document).ready(function(){

    display_sales_list(data)


    $("#submit_sale").click(function(){
        submitSale()
    })

    $("#enter_reams").keypress(function(e){
        if(e.which == 13) { //13 is the enter button
            submitSale()
        }
    })

    $("#view_result_button").click(function (e) {
         console.log("view result button clicked")
         e.preventDefault()
         redirect()




        })


})


//
//
// function display_sales_list2(sales){
//
//     let sr = $(".salesrep");
//     let c = $(".client");
//     let r = $(".reams");
//     $.each(sales, function(index, value){
//        console.log(index+value);
//        $.each(value, function(index2, value2) {
//            console.log("dictionary item: " + index2+value2); // this is printing correctly
//            // show prepop data in ui
//            if(index2=="salesperson"){
//                sr.append(
//                    "<div class=container><span>"+value2+"</span><br></br></div>"
//                );
//            }
//            else if(index2=="client"){
//                c.append(
//                    "<div class=container><span>"+value2+"</span><br></br></div>"
//                );
//            }
//            else {
//                r.append(
//                    "<div class=container><span>"+value2+"</span><br></br></div>"
//                );
//            }
//
//
//        });
//
//    })
// };