const chrome = require('chrome');
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#submit').addEventListener('click', function() {
        chrome.notifications.create('ping', {
            type: 'basic',
            iconUrl: 'pinger.png',
            title: 'Update!',
            message: 'A website you are tracking has been updated!',
            priority: 2
        });
    });

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
