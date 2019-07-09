var rssData = $(".rss_data");
var jpost = $("#jpost");
var geek = $("#geek");
var nba = $("#nba");
var update = $(".updated")

var time = document.cookie.substring(document.cookie.indexOf("update=") + 8)
var realTime = time.split(".")[0]
update.html("Last Update: " + realTime)

jpost.click(function(){
    rssData.html("")
    rssData.removeClass("hide")
    $.ajax({
        type: "GET",
        url: "http://localhost:7000/jpost",
        dataType: "JSON",
        success: function(response) {
            for (let i = 0; i < response.length; i++) {
                var insert = $("<li>")
                var link = $("<a>")
                link.text(response[i].title)
                link.attr("href",response[i].link)
                insert.append(link)
                rssData.append(insert)
            }
        }
    })
})

geek.click(function(){
    rssData.html("")
    rssData.removeClass("hide")
    $.ajax({
        type: "GET",
        url: "http://localhost:7000/geek",
        dataType: "JSON",
        success: function(response) {
            for (let i = 0; i < response.length; i++) {
                var insert = $("<li>")
                var link = $("<a>")
                link.text(response[i].title)
                link.attr("href",response[i].link)
                insert.append(link)
                rssData.append(insert)
            }
        }
    })
})

nba.click(function(){
    rssData.html("")
    rssData.removeClass("hide")
    $.ajax({
        type: "GET",
        url: "http://localhost:7000/nba",
        dataType: "JSON",
        success: function(response) {
            for (let i = 0; i < response.length; i++) {
                var insert = $("<li>")
                var link = $("<a>")
                link.text(response[i].title)
                link.attr("href",response[i].link)
                insert.append(link)
                rssData.append(insert)
            }
        }
    })
})

$('#reload').click(function() {
    location.reload();
});