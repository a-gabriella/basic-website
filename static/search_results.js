function clearResults(){
    //empty old data
    $("#search_results").empty()
    console.log("cleared!")
}

function clearQuery(){
    $("#search_query_display").empty()
     $("#search_query_display").append("Search results for")
}


function displaySearchResults(data, query, regions_matched, cusine_matched){
    console.log("search button pressed")
    clearResults()
    console.log("data going to search results.js")
    console.log(data)
    let title_header = ("<br><br><h6><u>"+"Title matche(s) found"+"</u></h6>")
    $("#search_results").append(title_header)
    $.each(data, function(i, datum){
        let title = datum["title"]
        let link = datum["link"]
        if(data == "no match") {
            $("#search_results").append(data)
        }
        else {
            let title_highlighted = title.replace(new RegExp(query, "ig"), (match) => `<SPAN STYLE="font-weight:900">${match}</SPAN>`);
            let new_result = $("<div><a href=\"" + link + "\">" + title_highlighted + "</a></div>")
            $("#search_results").append(new_result)
        }
    })

    let region_header = ("<br><br><h6><u>"+"Region matche(s) found"+"</u></h6>")
    $("#search_results").append(region_header)
    $.each(regions_matched, function(i, datum2){
        let title = datum2["title"]
        let region = datum2["region"]
        let link = datum2["link"]
        if(regions_matched == "no match") {
            $("#search_results").append(regions_matched)
        }
        else {
            let region_highlighted = region.replace(new RegExp(query, "ig"), (match) => `<SPAN STYLE="font-weight:900">${match}</SPAN>`);
            let new_result= $("<div><a href=\""+link+"\">"+region_highlighted+" </a><i>("+title+")</i></div>")
            $("#search_results").append(new_result)
        }

    })
    let cusine_header = ("<br><br><h6><u>"+"Cuisine matche(s) found"+"</u></h6>")
    $("#search_results").append(cusine_header)
    $.each(cusine_matched, function(i, datum3){
        let title = datum3["title"]
        let cusine = datum3["cuisine"]
        let link = datum3["link"]
        if(cusine_matched == "no match") {
            $("#search_results").append(cusine_matched)
        }
        else {
            let cusine_highlighted = cusine.replace(new RegExp(query, "ig"), (match) => `<SPAN STYLE="font-weight:900">${match}</SPAN>`);
            let new_result= $("<div><a href=\""+link+"\">"+cusine_highlighted+" </a><i>("+title+")</i></div>")
            $("#search_results").append(new_result)
        }

    })
}




$(document).ready(function(){
    console.log("in searchresults.js")
    displaySearchResults(data, query, regions_matched, cusine_matched)
    console.log("data query regions matched")
    console.log(regions_matched)
    console.log("submit2in searchresults.js")

    })

