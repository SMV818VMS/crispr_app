# Import Flask framework
# -------------------------------------------------------------------
from flask import Flask, request, redirect, url_for, g

# Import Blueprints
# -------------------------------------------------------------------
from .crispr_app.views import crispr_app

# Start Flask
# -------------------------------------------------------------------
app = Flask(__name__)

# Register Blueprints
# -------------------------------------------------------------------
app.register_blueprint(crispr_app, url_prefix='/crispr')
