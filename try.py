from app import app, db, models

dbs = db.session

clients = models.Client.query.filter_by(telegram_id=111)

print clients
print clients.count()

c = models.Client(telegram_id=123, 
                 username='username',
                 first_name='first_name',
                 last_name='last_name')
dbs.add(c)
dbs.commit()

clients = models.Client.query.filter_by(telegram_id=123)
print clients
print clients.count()