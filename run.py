from app import create_app
import logging

app = create_app()

# Add error handling
@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Server Error: {error}")
    return "500 error", 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    logging.error(f"Unhandled Exception: {e}")
    return "500 error", 500

if __name__ == '__main__':
    app.run(debug=True)