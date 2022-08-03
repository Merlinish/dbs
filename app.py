from flask import Flask,request,render_template
import joblib
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1=joblib.load("regression")
        model2=joblib.load("tree")
        a=model1.predict([[rates]])
        b=model2.predict([[rates]])
        return(render_template("index.html",result1=a,result2=b))
    else:
        return(render_template("index.html",result1="Waiting",result2="Waiting"))
if __name__ == "__main__":
    app.run() 
