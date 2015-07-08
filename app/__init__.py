# Import Flask framework
# -------------------------------------------------------------------
from flask import Flask, request, redirect, url_for, g

# Import Blueprints
# -------------------------------------------------------------------
from .main_app.views import main_app

# Start Flask
# -------------------------------------------------------------------
app = Flask(__name__)

# Register Blueprints
# -------------------------------------------------------------------
app.register_blueprint(main_app, url_prefix='/crispr')
