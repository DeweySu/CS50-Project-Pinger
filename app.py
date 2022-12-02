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



