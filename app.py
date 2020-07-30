from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/your_url",methods=['GET','POST'])
def yoururl():
    if request.method=='POST':
        return render_template('your_url.html',code=request.form['code'])
    else:
        return redirect(url_for('home'))
