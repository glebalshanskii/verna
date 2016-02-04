from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    try:
        return render_template("index.html")
    except Exception, e:
        return(str(e))
        
@app.route('/purchase/<uid>')
def purchase(uid):
	try:
		return render_template("purchase.html", uid=uid)
	except Exception, e:
		return(str(e))
  
@app.route('/paypal_success/', methods=['POST', 'GET'])
#@crossdomain(origin='*')
def success():
	try:
		return render_template("success.html")
	except Exception, e:
		return(str(e))
  
@app.route('/paypal_failure/',  methods=['POST', 'GET'])
#@crossdomain(origin='*')
def failure():
	try:
		return render_template("failure.html")
	except Exception, e:
		return(str(e))
