from flask import Blueprint, render_template, redirect

root_app = Blueprint('root_app', __name__,
                     template_folder='templates',
                     static_folder='static')

@root_app.route('/')
def main():
    return redirect('/crispr')
