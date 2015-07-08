from flask import Blueprint, render_template, send_from_directory, url_for
import pandas as pd
import os

main_app = Blueprint('main_app', __name__,
                     template_folder='./templates/',
                     static_folder='./static/')

@main_app.route('/')
def main():
    path_to_table = '/home/alvaro/Repos/crispr_app/app/main_app/static/total_processed.txt'
    df = pd.read_csv(path_to_table, sep='\t', index_col=None)
    return render_template("index.html", dataframe=df)

@main_app.route('/sayhello/<name>')
def sayhello(name):
    return render_template("hello.html", name=name)

@main_app.route('/table/<column>/<value_min>-<value_max>')
def return_filtered_table(column, value_min, value_max):
    return 'Filtering by column {}: from {} to {}'.format(column,
            value_min, value_max)

@main_app.route('/table/')
def return_whole_table():
    return main_app.send_static_file('total_processed.json')
