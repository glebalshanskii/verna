import flask
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.datastructures import ImmutableOrderedMultiDict
import requests
from config import WEBHOOK_URL_PATH
import telebot
from config import API_TOKEN
import logging
logging.basicConfig(filename='verna.log',level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
logging.debug("db session init: "+str(db.session))

bot = telebot.TeleBot(API_TOKEN)

from app import views, models

# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data()
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_messages([update.message])
        return ''
    else:
        flask.abort(403)

@app.route('/paypal_ipn/',methods=['POST'])
def ipn():
	try:
		arg = ''
		flask.request.parameter_storage_class = ImmutableOrderedMultiDict
		values = flask.request.form
		for x, y in values.iteritems():
			arg += "&{x}={y}".format(x=x,y=y)

		validate_url = 'https://www.sandbox.paypal.com' \
					   '/cgi-bin/webscr?cmd=_notify-validate{arg}' \
					   .format(arg=arg)
		r = requests.get(validate_url)
		if r.text == 'VERIFIED':
			try:
				payer_email = flask.request.form.get('payer_email')
				unix = int(time.time())
				payment_date = flask.request.form.get('payment_date')
				username = flask.request.form.get('custom')
				last_name = flask.request.form.get('last_name')
				payment_gross = flask.request.form.get('payment_gross')
				payment_fee = flask.request.form.get('payment_fee')
				payment_net = float(payment_gross) - float(payment_fee)
				payment_status = flask.request.form.get('payment_status')
				txn_id = flask.request.form.get('txn_id')
			except Exception as e:
				with open('/tmp/ipnout.txt','a') as f:
					data = 'ERROR WITH IPN DATA\n'+str(values)+'\n'
					f.write(data)
			
			with open('/tmp/ipnout.txt','a') as f:
				data = 'SUCCESS\n'+str(values)+'\n'
				f.write(data)

#			c.conn = connection()
#			c.execute("INSERT INTO ipn (unix, payment_date, username, last_name, payment_gross, payment_fee, payment_net, payment_status, txn_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
#						(unix, payment_date, username, last_name, payment_gross, payment_fee, payment_net, payment_status, txn_id))
#			conn.commit()
#			c.close()
#			conn.close()
#			gc.collect()

		else:
			 with open('/tmp/input.txt','a') as f:
				data = 'FAILURE\n'+str(values)+'\n'
				f.write(data)
				
		return r.text
	except Exception as e:
		return str(e)
       
