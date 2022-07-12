from flask import Flask


app = Flask(__name__)
# configuramos para el uso de CSRF y SECRET_KEY
app.config.from_prefixed_env()