from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)

# If you want to customize Jinja2 settings in Flask, you can do so here
env = Environment(
    loader=PackageLoader("yourapp"),  # Your package or template folder
    autoescape=select_autoescape(["html", "xml"])  # Enable auto-escaping
)
app.jinja_env = env  # Optionally override Flask's default Jinja environment

@app.route('/')
def home():
    return render_template("index.html", title="Home Page")

if __name__ == "__main__":
    app.run(debug=True)
