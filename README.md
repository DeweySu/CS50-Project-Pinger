# CS50-Project-Pinger
Pinger is a web app that notifies users whenever selected webpages are updated. 

# Installation

For this app to run properly, you'll need to install several libraries (on top of the libraries and packages required for CS50). Run the following commands in your CS50 terminal:

```
# Validators library
pip3 install validators

# Requests library
pip3 install requests

# BeautifulSoup library
pip3 install beautifulsoup4
```

From there, install the code files in this GitHub repository, and enter the following into your terminal:
```
cd CS50-Project-Pinger
```
From there, just run this line in your terminal:
```
CS50-Project-Pinger/ $ flask run
```
and open the resulting link.

# Instructions

If you wish to monitor changes to a webpage, simply copy-and-paste the URL of said webpage into the input field on our web app and submit. You can also add a name for this website--this feature is wholly optional, and if no name is inputted, the title will be selected from the webpage's HTML. Any chosen webpages will then be added to the table on our app, and even if the web app is closed, the monitored webpages will remain in that table. (Unfortunately, no notifications will pop up when the app is closed.) Beyond the name of the website and its URL, our table also contains a "Last Updated" column. When the webpage is added, this "Last Updated" column will first record the time when that webpage was added to the table, but any change to the webpage will result in said column recording the date and time when that webpage was last updated in UTC. Note that this web app only works for webpages which do not require login information!

[!Here's an image of Pinger working properly!](https://github.com/DeweySu/CS50-Project-Pinger/blob/main/PingerScreenshot.jpg)

From there, the app will check every 30 seconds to see if anything on that webpage has been changed. If an update arises, a browser notification will pop up, and the names of which websites have been updated will appear in that notification. Note that any changes to the monitored webpage will result in a notification, no matter how minor the change, so beware of that! If you wish to stop monitoring a webpage, simply press the 'Remove' button next to its row in the table. This will delete the entire row, and no further notifications related to that webpage will be given. 
