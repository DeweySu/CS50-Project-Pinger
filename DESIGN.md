# Design of Pinger

Pinger was implemented as a Flask web app that was ultimately a potpourri of Python, HTML, CSS, JavaScript, SQL, and Jinja.

# ```app.py```
The principal tasks handled in ```app.py``` were server-side functions that allow the user to add and remove URLs from the table of websites they wish to track and monitor for updates. Courtesy of ```SQL``` from the ```cs50``` library, we were able to give the user a great deal of freedom to add, remove, and have tracked websites remain saved in the "Websites to Monitor" table even after closing the tab (i.e. when they no longer wish to track any websites and are done with using the app for now), as by writing ```db = SQL("sqlite:///websites_monitored.db")``` and then executing the appropriate SQL commands to update the table with information on the site name, inputted URL (provided it is valid, as checked by ```validators.url``` from the validators library). The way that we designed
