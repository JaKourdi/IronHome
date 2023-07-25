import os
from flask import Flask
from routes import order, auth, user
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level (other options: DEBUG, WARNING, ERROR, CRITICAL)
    filename='app.log',  # Specify the log file name
    filemode='a',  # 'a' for append mode, 'w' for overwrite mode
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Define the date-time format for log messages
)

app = Flask(__name__)
app.secret_key = 'TOP_SECRET'
app.register_blueprint(order.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(user.bp)
app.add_url_rule("/", endpoint="index")
env = os.environ.get('FLASK_ENV', 'development')
secret_key = os.environ.get('SECRET_KEY', 'dev-secret')
port = int(os.environ.get('PORT', 5000))
debug = False if env == 'production' else True
app.config['SECRET_KEY'] = secret_key


@app.route("/hello")
def hello():
    return "Hello, Unity!"


if __name__ == "__main__":
    app.config['DEBUG'] = debug
    app.run(host='0.0.0.0', port=port, debug=debug)

