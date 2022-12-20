#First we import librarires
from flask import * 

# Intiallize Flask function
app = Flask(__name__)
app.secret_key = "GeeksForGeeks"


#home function for index.html
@app.route("/index")
def home():
    return render_template("index.html")

#login function for index2.html
@app.route("/index2")
def login():
    return render_template("index2.html")

#row function for index3.html
@app.route("/index3")
def row():
    return render_template("index3.html")

# execute command with debug function
if __name__ == '__main__':
    app.run(debug=True)

