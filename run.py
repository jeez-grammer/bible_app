from app import create_app
import logging

app = create_app()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        logger.error(f"Error starting the Flask app: {e}", exc_info=True)