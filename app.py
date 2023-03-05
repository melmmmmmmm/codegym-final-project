import os

from flask import Flask, render_template, request
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
    else:
        selected_color_code = request.form.get("selected_color_code")
        conn = sqlite3.connect('color.db')
        c = conn.cursor()
        c.execute('SELECT matching_color_name, matching_color_code FROM color_matches WHERE color_code = ?', (selected_color_code,))
        matches_colors = []
        for row in c.fetchall():
            matches_colors.append({'matching_color_name': row[0], 'matching_color_code': row[1]})
        c.close()
        return render_template("selected.html", matches_colors=matches_colors)

if __name__ == '__main__':
    app.run(debug=True)
