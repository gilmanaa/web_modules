var rssData = $(".rss_data");

$(document.body).ready(function(){
    $.ajax({
        type: "GET",
        url: "http://localhost:7000/feed",
        dataType: "JSON",
        success: function(response) {
            for (let i = 0; i < response.length; i++) {
                var insert = $("<div>")
                var link = $("<a>")
                link.text(response[i].title)
                link.attr("href",response[i].link)
                insert.append(link)
                rssData.append(insert)
            }
        }
    })
})