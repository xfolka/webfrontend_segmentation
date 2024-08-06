# my_flask_app.py

from flask import Flask, render_template, request, url_for
import os
import io
import tifffile
import numpy as np
app = Flask(__name__, static_folder='static')

app.config['UPLOAD_FOLDER'] = "uploads/"

###################
## REST API ##
###################

API_PREFIX = "/CCI_API"

allowedFileEndings = [".tiff", ".png", "jpg"]
@app.route(API_PREFIX + '/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        en = request.content_length
        enc = request.content_encoding
        data = request.get_data()
#        fileKey = request.files.keys()
#        file = request.files[fileKey]

        if data != None:
            tifdata = tifffile.imread(io.BytesIO(np.array(data)))
            tifffile.imwrite(app.config['UPLOAD_FOLDER'] + "test2.tiff",tifdata)
            #with open(app.config['UPLOAD_FOLDER'] + "test.tiff", "wb") as file:
            #    file.write(data);

#            tifffile.imwrite(app.config['UPLOAD_FOLDER'] + "test.tiff", np.array(data), photometric='minisblack')
            #tifffile.imwrite(app.config['UPLOAD_FOLDER'] + "test.tiff",io.BytesIO(data))
            return url_for('uploaded_file',
                filename="test.tiff")

        # if file:
        #     print('**found file ' + file.filename)
        #     filename = (file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     # for browser, add 'redirect' function on top of 'url_for'
            return url_for('uploaded_file',
                                    filename=filename)


allowedFileEndings = [".tiff", ".png", "jpg"]
@app.route(API_PREFIX + '/ltest', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        en = request.content_length
        enc = request.content_encoding
        data = request.get_data()
#        fileKey = request.files.keys()
#        file = request.files[fileKey]

        if data != None:
            tifdata = tifffile.imread(io.BytesIO(np.array(data)))
            tifffile.imwrite(app.config['UPLOAD_FOLDER'] + "test2.tiff",tifdata)
            #with open(app.config['UPLOAD_FOLDER'] + "test.tiff", "wb") as file:
            #    file.write(data);

#            tifffile.imwrite(app.config['UPLOAD_FOLDER'] + "test.tiff", np.array(data), photometric='minisblack')
            #tifffile.imwrite(app.config['UPLOAD_FOLDER'] + "test.tiff",io.BytesIO(data))
            return url_for('uploaded_file',
                filename="test.tiff")

        # if file:
        #     print('**found file ' + file.filename)
        #     filename = (file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     # for browser, add 'redirect' function on top of 'url_for'
            return url_for('uploaded_file',
                                    filename=filename)


###################
## Static routes ##
###################

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/input")
def input_file():
    return render_template('input_file.html', api_prefix=API_PREFIX)


if __name__ == "__main__":
    app.run()
