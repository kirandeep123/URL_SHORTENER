from flask import Flask,render_template,request,redirect,url_for,flash
import json
import os.path
# from werkzeug import secure_filename
app = Flask(__name__)
app.secret_key="sdnfbsmdnfvsbdvfbds"
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/your_url",methods=['GET','POST'])
def yoururl():
    if request.method=='POST':
        urls={}

        if(os.path.exists('url.json')):
            with open('url.json') as urls_file:
                urls = json.load(urls_file)
        if request.form['code'] in urls.keys():
            flash("That code has already been taken ")
            return redirect(url_for('home'))
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + f.filename
            f.save('/Users/kirandeepkaur/Desktop/url-shortener/'+full_name)
            urls[request.form['code']] = {'file':full_name}


        with open('url.json','w') as url_file:
            json.dump(urls,url_file)
        return render_template('your_url.html',code=request.form['code'])
    else:
        return redirect(url_for('home'))
