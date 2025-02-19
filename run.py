from app import create_app
import logging
import traceback

app = create_app()

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Add a simple route for testing
@app.route('/test')
def test():
    return "Test route is working!"

# Add error handling
@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Server Error: {error}")
    logging.error(traceback.format_exc())
    return "500 error", 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    logging.error(f"Unhandled Exception: {e}")
    logging.error(traceback.format_exc())
    return "500 error", 500

if __name__ == '__main__':
    app.run(debug=True)