async function addWebsite() {
    let url_to_add = document.getElementById("newURL").value;
    const res=await fetch (url_to_add);
    const res_text = res.text();

    var tableRow = document.getElementById("websiteTable");
    var row = document.createElement("tr");
    var name = document.createElement("td");
    var url = document.createElement("td");
    var last_updated = document.createElement("td");
    name.innerHTML = res_text.title;
    cell2.innerHTML = url_to_add;
    cell3.innerHTML = "N/A";
    row.appendChild(cell1);
    row.appendChild(cell2);
    row.appendChild(cell3);
    tableRow.appendChild(row);
}
addWebsite();
/*
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#temp').addEventListener('click', function() {
        chrome.notifications.create('ping', {
            type: 'basic',
            iconUrl: 'pinger.png',
            title: 'Update!',
            message: 'A website you are tracking has been updated!',
            priority: 2
        });
    });
});
*/
/* Getting title from URL (probably not complete) | Source: https://stackoverflow.com/questions/60291497/is-there-a-way-to-get-a-websites-full-title-from-the-google-custom-search-api
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false ); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

httpGet('https://youtube.com', function(response) {
    // parse the title tag here
});
*/

/*
chrome.alarm.create('testAlarm', {
	periodInMinutes: 1440
});
*/
