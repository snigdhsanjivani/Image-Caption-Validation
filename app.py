from flask import Flask, render_template, url_for, request, redirect
# from flask_mysqldb import MySQL
from verify import *

app = Flask(__name__) 
 

@app.route('/')
def index():
    # randomly or orderly(as per need) select an image from dataset and pass it to index.html
    # return render_template('index.html', img = img_sel)    
    return render_template('index.html')

# @app.route("/predict/<int :id>", methods=['GET', 'POST'])
# def predict(id):
#     if(request.method == 'POST'):
#         get data from id, extract image
#         caption_pred = predict_caption()
#         input_desc = request.form['desc']
#         isTrue = verify_desc(input_desc, caption_pred)
#     return render_template("index.html", result = isTrue) 

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    # initialize model
    if(request.method == 'POST'):
        input_desc = request.form['desc']
        isTrue = verify_desc(input_desc)
    return render_template("index.html", result = isTrue) 


if __name__=='__main__':
    app.run(debug=True)



    """
    to use commented code, database required

    [summary]
    start-> Select a random image from database
    Send it to frontend
    Get the description from form
    Evaluate it against the generated caption
    Correct or Incorrect accordingly
    Try again -> back to start

    [scripts]
    description_generator.py(test)
    description_verify.py(test)
    """
