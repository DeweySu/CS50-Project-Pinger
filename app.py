# IMPORTANT: when testing, make sure that index.html is within a templates folder
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from datetime import datetime
import validators
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

"""
A SQL database to store the websites we're monitoring

Schema:
CREATE TABLE Websites (
  name TEXT,
  url TEXT UNIQUE,
  last_updated datetime,
  hash numeric
);
"""
db = SQL("sqlite:///websites_monitored.db")

@app.route("/", methods=["GET", "POST"])
def index():
  # User reached route via POST (as by submitting a form via POST)
  if request.method == "POST":
    url = request.form.get("url")

    # If URL is invalid, redirect to main page and don't change anything
    if not validators.url(url):
      return redirect("/")

    # Get the content of a webpage
    webpage = requests.get(url)

    # Use BeautifulSoup to parse said webpage
    soup = BeautifulSoup(webpage.text, 'html.parser')

    if not request.form.get("name"):
        # Get title of webpage
        title = str(soup.find('title').string)

    else:
        title = request.form.get("name")

    # Hash contents of webpage for future comparison
    current_hash = hash(webpage.text)

    # Insert data into SQLite table
    try:
      db.execute("INSERT INTO Websites (name, url, last_updated, hash) VALUES (?, ?, ?, ?);", title, url, datetime.now(), current_hash)
    except:
      pass
    return redirect("/")

  # User reached route via GET (as by clicking a link or via redirect)
  else:
    websites_monitored = db.execute("SELECT * FROM Websites;")
    for website in websites_monitored:
      initial_hash = website['hash']
      current_hash = hash(requests.get(website['url']).text)
      website_url = website['url']
      if initial_hash != current_hash:
        # flash("W")
        db.execute("UPDATE Websites SET hash = ?, last_updated = ? WHERE url = ?", current_hash, datetime.now(), website_url)
    return render_template("index.html", websites_monitored=websites_monitored)

@app.route("/remove", methods=["POST"])
def remove():

    # Forget website
    url = request.form.get("url")
    if url:
        db.execute("DELETE FROM websites_monitored WHERE url = ?", url)
    return redirect("/")
