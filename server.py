from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route("/templates/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
#
#
# @app.route("/templates/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/templates/project.html")
# def project():
#     return render_template('project.html')
#
# @app.route("/templates/index.html")
# def index():
#     return render_template('index.html')

# @app.route("/favicon.ico")
# def data():
#     return "<p>This is where datasets will live!</p>"