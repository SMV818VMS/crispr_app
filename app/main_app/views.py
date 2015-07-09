from flask import Blueprint, render_template, send_from_directory, url_for, request, g
import pandas as pd
import os

main_app = Blueprint('main_app', __name__,
                     template_folder='./templates/',
                     static_folder='./static/')

ROWS_PER_PAGE = 500
# PATH_TO_TABLE = '/home/alvaro/Repos/crispr_app/app/main_app/static/total_processed.txt'
PATH_TO_TABLE = '/home/samiver/projects/webs/app/main_app/static/total_processed.txt'

def modify_dataframe(dataframe, minimum='', maximum='',
                     col_filter='', col_order='', asc=''):
    df = dataframe
    if col_filter and not col_filter in df.columns:
        return df
    if col_order and not col_order in df.columns:
        return df

    if minimum or maximum:
        try:
            minimum = int(float(minimum))
            maximum = int(float(maximum))
        except:
            return df

    if col_filter != '' and minimum != '' and maximum != '':
        # filter the table
        df = df[(df[col_filter] >= minimum) & (df[col_filter] <= maximum)]
        table_size = df.shape[0]

    if col_order != '':
        # order the table
        df = df.sort(columns=[col_order], ascending=asc)

    return df



@main_app.route('/')
def main():
    path_to_table = PATH_TO_TABLE
    df = pd.read_csv(path_to_table, sep='\t', index_col=None)

    minimum = request.args.get('min', '')
    maximum = request.args.get('max', '')
    col_filter = request.args.get('filterby', '')
    col_order = request.args.get('orderby', '')
    # change order from ascending to descending on consecutive clicks
    asc = False if request.args.get('asc', '') == 'False' else True
    page = request.args.get('page', '0')

    df = modify_dataframe(dataframe=df, minimum=minimum, maximum=maximum,
                          col_filter=col_filter, col_order=col_order,
                          asc=asc)
    table_size = df.shape[0]

    try:
        page = int(page)
    except:
        page = 0

    from_row = page * ROWS_PER_PAGE
    to_row = from_row + ROWS_PER_PAGE
    df = df[from_row:to_row]
    return render_template("index.html", dataframe=df,
                    inputs={'filterby': col_filter, 'min': str(minimum),
                            'max': maximum, 'page': page, 'asc': asc,
                            'rows_per_page': ROWS_PER_PAGE,
                            'orderby': col_order,
                            'page_span': (from_row, to_row),
                            'table_size': table_size})

@main_app.route('/download/')
def download():
    path_to_table = PATH_TO_TABLE
    df = pd.read_csv(path_to_table, sep='\t', index_col=None)

    minimum = request.args.get('min', '')
    maximum = request.args.get('max', '')
    col_filter = request.args.get('filterby', '')
    col_order = request.args.get('orderby', '')
    # change order from ascending to descending on consecutive clicks
    asc = False if request.args.get('asc', '') == 'False' else True
    page = request.args.get('page', '0')

    df = modify_dataframe(dataframe=df, minimum=minimum, maximum=maximum,
                          col_filter=col_filter, col_order=col_order,
                          asc=asc)
    return df.to_csv()

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
