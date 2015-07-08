from flask import Blueprint, render_template, send_from_directory, url_for, request
import pandas as pd
import os

main_app = Blueprint('main_app', __name__,
                     template_folder='./templates/',
                     static_folder='./static/')

@main_app.route('/')
def main():
    path_to_table = '/home/alvaro/Repos/crispr_app/app/main_app/static/total_processed.txt'
    df = pd.read_csv(path_to_table, sep='\t', index_col=None)
    minimum = request.args.get('min', '')
    maximum = request.args.get('max', '')
    column = request.args.get('column', '')

    if not column in df.columns:
        return "Wrong column: {}".format(column)

    try:
        minimum = int(float(minimum))
        maximum = int(float(maximum))
    except:
        return "Minimum value and maximum value must be numbers"

    df = df[(df[column] >= minimum) & (df[column] <= maximum)]

    return render_template("index.html", dataframe=df[:500])

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
