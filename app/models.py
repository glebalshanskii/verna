from datetime import datetime
from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    telegram_id = db.Column(db.Integer, index=True, unique=True, nullable=False)
    username = db.Column(db.String(256), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(256), index=True, nullable=False)
    last_name = db.Column(db.String(256), index=True, nullable=False)
#    isExpert = db.Column(db.Boolean, index=True, nullable=False)
#    AboutLink = db.Column(db.String(256), index=True, default='')
#    ActiveUserId = db.Column(db.Integer, index=True)
#    UserChatId = db.Column(db.Integer, index=True)
#    ExpertChatId = db.Column(db.Integer, index=True)
    
    payments = db.relationship("Payment", backref="client")
    tickets = db.relationship("Ticket", backref="client")
    
    def __init__(self, telegram_id=None, username=None, first_name=None, last_name=None):
        self.name = telegram_id=telegram_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return '<Client %r>' % (self.username)
        
class Expert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    telegram_id = db.Column(db.Integer, index=True, unique=True, nullable=False)
    username = db.Column(db.String(256), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(256), index=True, nullable=False)
    last_name = db.Column(db.String(256), index=True, nullable=False)
    youtube_link = db.Column(db.String(), index=True, default='')
    youtybe_video_id = db.Column(db.String(), index=True, default='')
    paypal_id = db.Column(db.String(), index=True, default='')
    
    links = db.relationship("Link", backref="expert")

    def __init__(self, telegram_id=None, username=None, first_name=None, last_name=None):
        self.name = telegram_id=telegram_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return '<Expert %r>' % (self.username)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    url = db.Column(db.String(), index=True, default='')
    
    expert_id = db.Column(db.Integer, db.ForeignKey('expert.id'))

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    paypal_id = db.Column(db.String(), index=True, default='')
    payment_gross = db.Column(db.Float, index=True)
    payment_fee = db.Column(db.Float, index=True)
    payment_net = db.Column(db.Float, index=True)
    payment_status = db.Column(db.String(), index=True, default='')
    txn_id = db.Column(db.String(), index=True, default='')
    
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)    
    amount = db.Column(db.Float, index=True)
    duration = db.Column(db.Integer, index=True)
    
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    expert_id = db.Column(db.Integer, db.ForeignKey('expert.id'))
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    raw_message = db.Column(db.String(), index=True, default='')   

