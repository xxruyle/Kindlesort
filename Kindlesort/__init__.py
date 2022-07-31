import os 
from flask import Flask, flash, request, redirect, url_for, render_template, session 
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'Kindlesort/upload'
ALLOWED_EXTENSIONS = {"txt"}
SECRET_KEY = "6968"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

app.config['SECRET_KEY'] = SECRET_KEY

import Kindlesort.views 