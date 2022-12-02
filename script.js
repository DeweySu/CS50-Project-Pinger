// Potential APIs: https://developer.chrome.com/docs/extensions/reference/
// Tasks: get relevant extension APIs (e.g. chrome.alarms, chrome.notifications), get website title from URL and update table in index.html accordingly
// Make the API requests here!

// add the below into conditional (e.g. if hash has changed, execute the below lines of code)
chrome.notifications.create('ping', {
    type: 'basic',
    iconUrl: 'pinger.png',
    title: 'Update!',
    message: 'A website you are tracking has been updated!',
    priority: 2
});

// Getting title from URL (probably not complete) | Source: https://stackoverflow.com/questions/60291497/is-there-a-way-to-get-a-websites-full-title-from-the-google-custom-search-api
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

httpGet('http://some/url', function(response) {
    // parse the title tag here
});
