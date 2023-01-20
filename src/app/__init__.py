from pathlib import Path
from random import choice
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g

app = Flask(__name__)

@app.before_first_request
def get_fonts():
    font_dir = Path(__file__).parent.parent / 'fonts'
    g.fonts = [f.name for f in font_dir.iterdir() if f.is_file()]
    app.logger.info(f'Found {len(g.fonts)} local fonts')
    app.logger.debug(f'Fonts: {g.fonts}')

@app.before_first_request
def get_images():
    image_dir = Path(__file__).parent.parent / 'images'
    g.images = [f.name for f in image_dir.iterdir() if f.is_file()]
    app.logger.info(f'Found {len(g.images)} local images')
    app.logger.debug(f'Images: {g.images}')

@app.route('/')
def index():
    app.logger.debug(g.fonts)
    app.logger.debug(g.images)
    return 'Hello, World!'