# IMPORTANT: when testing, make sure that index.html is within a templates folder
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

import re
from datetime import datetime

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# A SQL database to store the websites we're monitoring
# Columns are name, URL, times last updated, and the hash
db = SQL("sqlite:///websites_monitored.db")
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
  # User reached route via GET (as by clicking a link or via redirect)

  # User reached route via POST (as by submitting a form via POST)
  if request.method == "POST":
    url = request.form.get("username")
    if not url:
      return redirect("/")
    # Next steps: find out how to get website name and how to hash the URL
    db.execute("INSERT INTO Websites (url) VALUES (?)", url)
    return redirect("/")
  else:
    websites_monitored = db.execute("SELECT DISTINCT * FROM Websites")
    return render_template("index.html", websites_monitored=websites_monitored)

"""
if update...:
    flash("Ping! One of your websites has changed.")

