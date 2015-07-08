from flask import Blueprint, render_template

other_app = Blueprint('other_app', __name__,
                      template_folder='./templates',
                      static_folder='./static')

@other_app.route('/')
def main():
    return render_template("index.html")

@other_app.route('/sayhello/<name>')
def sayhello(name):
    return render_template("hello.html", name=name)
