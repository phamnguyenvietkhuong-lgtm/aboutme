from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)
@app.route("/mis")
def course():
  return "<h1>資訊管理導論</h1>"
@app.route("/today")
def today():
  now = datetime.now()
  return render_template("today.html", datetime=str(now))
@app.route("/about")
def about():
    return "<h1>范阮越姜Python網頁</h1><p>帐号:[411314725]<p>"
if __name__ == "__main__":
   app.run()
  