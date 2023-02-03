from flask import Flask, request, render_template
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    search_term = request.form["search_term"]
    if len(search_term) < 3:
        return render_template("index.html", search_term=search_term)
    else:
        match = False
        suggestions = []
        with open('static\databas\mediciner.csv', newline='') as csvfile:
            data = list(csv.reader(csvfile))
            for row in data:
                for col in row:
                    if search_term.lower() in col.lower():
                        match = True
                        suggestions.append(col)
        if match:
            return render_template("results.html", match=match, suggestions=suggestions, search_term=search_term)
        else:
            return render_template("results.html", match=match, suggestions=suggestions, search_term=search_term)

@app.route("/usage")
def usage():
    return render_template("usage.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/mediciner")
def mediciner():
    with open('static\databas\mediciner.csv', 'r') as file:
        content = file.read()
    return content

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()
