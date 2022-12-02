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


