import os 
from flask import Flask, flash, request, redirect, url_for, render_template
from Kindlesort import app, ALLOWED_EXTENSIONS
from werkzeug.utils import secure_filename

def allowed_file(filename): 
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        
@app.route("/") 
def home(): 
    '''The base template'''
    return render_template("base.html") 

@app.route("/home")
def index(): 
    '''The home template'''
    return render_template("home.html")

@app.route("/books", methods=['GET', 'POST'])  
def books(): 
    '''The template containing books, ability to upload myclippings'''
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('books.html')



    return render_template("books.html")