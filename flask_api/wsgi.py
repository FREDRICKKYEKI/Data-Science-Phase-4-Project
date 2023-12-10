import sys
import os

# Add the path to your application to the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Import your application
from app import app

# Define the application to be used by the WSGI server
application = app

# Optional: You can configure the WSGI server here
# For example, if using gunicorn, you can set the number of workers
# gunicorn -w 4 wsgi:application
