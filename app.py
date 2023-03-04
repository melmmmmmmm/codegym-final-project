import os

from flask import Flask, flash, redirect, render_template, request, session, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/get_matching_colors', methods=['POST'])
def get_matching_colors():
    selected_color = request.json['selectedColor']
    conn = sqlite3.connect('colors.db')
    c = conn.cursor()
    c.execute('SELECT matching_color FROM color_matches WHERE color = ?', (selected_color,))
    matching_colors = [row[0] for row in c.fetchall()]
    conn.close()
    return jsonify(matching_colors)

if __name__ == '__main__':
    app.run(debug=True)
