from flask import Flask, render_template, url_for, request, redirect
# from flask_mysqldb import MySQL
from verify import *

app = Flask(__name__) 
 
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'MyDB'
 
# mysql = MySQL(app)


# class ImgPath(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     path = db.Column(db.String(100), nullable = False)

#     def __repr__(self):
#         return '<Path %r>' %self.path

# isTrue = 1              #default value = -1; for correct->1; for incorrect->0


@app.route("/", methods=['GET', 'POST'])
def index():
    isTrue = 1
    if(request.method == 'POST'):
        input_desc = request.form['desc']
        print(input_desc)
        print("if1",isTrue)
        isTrue = verify_desc(input_desc) 
        print("if2",isTrue)
        return redirect("/")
    else:
        # isTrue = verify_desc(input_desc)
        print("else1", isTrue)
        isTrue = verify_desc(input_desc) 
        print("else2", isTrue)
        return render_template('index.html', result = isTrue)


if __name__=='__main__':
    app.run(debug=True)



    """
    [summary]
    start-> Select a random image from database
    Send it to frontend
    Get the description from form
    Evaluate it against the generated caption
    Correct or Incorrect accordingly
    Try again -> back to start

    [scripts]
    description_generator.py
    description_verify.py
    """
