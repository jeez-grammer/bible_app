from flask import Blueprint, render_template
from .utils.excel_reader import get_excel_data

main = Blueprint('main', __name__)
@main.route('/')
def index():
    data = get_excel_data()
    return render_template('index.html', data=data)