import os 
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'Kindlesort/upload'
ALLOWED_EXTENSIONS = {"txt"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

import Kindlesort.views 