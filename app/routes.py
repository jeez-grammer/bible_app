from flask import Blueprint, render_template
from .utils.excel_reader import get_excel_data
import logging

main = Blueprint('main', __name__)

@main.route('/')
def index():
    try:
        data = get_excel_data()
        return render_template('index.html', data=data)
    except Exception as e:
        logging.error(f"Error in index route: {e}", exc_info=True)
        return "Internal Server Error", 500