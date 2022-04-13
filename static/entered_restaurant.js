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

$(document).ready(function(){

    display_sales_list(data)


})