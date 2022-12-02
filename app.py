# For Flask (important: make sure all this stuff can be run by anyone!)
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

import re
from datetime import datetime

app = Flask(__name__)

# A SQL database to store the websites we're monitoring
# Columns are name, URL, times last updated, and the hash
db = SQL("sqlite:///websites_monitored.db")

@app.route("/")
def index():
  # User reached route via GET (as by clicking a link or via redirect)
  # User reached route via POST (as by submitting a form via POST)
  
  return render_template("index.html", websites_monitored=websites_monitored)

