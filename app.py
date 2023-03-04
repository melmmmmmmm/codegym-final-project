import os

from flask import Flask, flash, redirect, render_template, request, session, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        conn = sqlite3.connect('color.db')
        c = conn.cursor()
        c.execute('SELECT DISTINCT color_name, color_code FROM color_matches')
        colors = []
        for row in c.fetchall():
            colors.append({'color_name': row[0], 'color_code': row[1]})
        c.close()
        return render_template("index.html", colors=colors)
