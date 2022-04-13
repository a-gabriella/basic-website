function displayRestaurants(data){
    //empty old data
    $("#restaurant_container").empty()

    //insert all new data
    $.each(data, function(i, datum){
        console.log("I am in top_rest...js in displayRest...")
        console.log(datum)
        console.log(datum['1']['title'])
        let name = datum['1']['title']
        let link =  datum['1']['link']
        let picture = datum['1']['url']
        console.log(picture)
        let new_title= $("<a href=\"" + link + "\">"+name+"</a>")
        console.log(new_title)
        $("#card-title1").append(new_title)
        new_image = $("<a href=\"" + link + "\"><img src = \"" + picture + "\" alt=\"a picture of the restaurant\" width = 100% class=\"card-img-top\"></a>")
        $("#image1").append(new_image)
    })
        $.each(data, function(i, datum){
        console.log("I am in top_rest...js in displayRest...")
        console.log(datum)
        console.log(datum['2']['title'])
        let name = datum['2']['title']
        let link =  datum['2']['link']
        let picture = datum['2']['url']
        console.log(picture)
        let new_title= $("<a href=\"" + link + "\">"+name+"</a>")
        console.log(new_title)
        $("#card-title2").append(new_title)
        new_image = $("<a href=\"" + link + "\"><img src = \"" + picture + "\" alt=\"a picture of the restaurant\" width = 100% class=\"card-img-top\"></a>")
        $("#image2").append(new_image)
    })
        $.each(data, function(i, datum){
        console.log("I am in top_rest...js in displayRest...")
        console.log(datum)
        console.log(datum['3']['title'])
        let name = datum['3']['title']
        let link =  datum['3']['link']
        let picture = datum['3']['url']
        console.log(picture)
        let new_title= $("<a href=\"" + link + "\">"+name+"</a>")
        console.log(new_title)
        $("#card-title3").append(new_title)
        new_image = $("<a href=\"" + link + "\"><img src = \"" + picture + "\" alt=\"a picture of the restaurant\" width = 100% class=\"card-img-top\"></a>")
        $("#image3").append(new_image)
    })


}



$(document).ready(function(){
    //when the page loads, display all the names
    displayRestaurants(data)



})