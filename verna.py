from app import app, db, models, bot
from config import WEBHOOK_SSL_CERT, WEBHOOK_URL_BASE, WEBHOOK_URL_PATH, YOUTUBE_URL_REGEXP
import logging

logging.basicConfig(filename='verna.log',level=logging.DEBUG)
dbs = db.session
logging.debug("db session verna: "+str(db.session))
# url_regexp="http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

@bot.message_handler(commands=['start', 'help'])
def register_client(message):

    logging.debug('message /start')    
    logging.debug('message from user id: '+str(message.from_user.id))
    logging.debug('message: '+str(message))

    clients = models.Client.query.filter_by(telegram_id=message.from_user.id).all()
    
    logging.debug(str(clients))
    logging.debug(str(clients.count()))  
    
    if (clients.count() == 0):
#    if True:
#        c = models.Client(telegram_id=message.from_user.id, 
#                 username=message.from_user.username,
#                 first_name=message.from_user.first_name,
#                 last_name=message.from_user.last_name)
#        dbs.add(c)
#        dbs.commit()
        bot.reply_to(message, "Welcome!")
    else:
        bot.reply_to(message, "Welcome back!")
    logging.debug('register_client done')

@bot.message_handler(commands=['iamexpert'])
def register_expert(message):
    senders = models.Expert.query.filter_by(telegram_id=message.from_user.id)
    if (senders.count() == 0): 
        u = models.Expert(telegram_id=message.from_user.id, 
                 username=message.from_user.username,
                 first_name=message.from_user.first_name,
                 last_name=message.from_user.last_name)
        dbs.add(u)
        dbs.flush()
        dbs.commit()
        bot.reply_to(message, "You are expert now!")
    else:
        bot.reply_to(message, "You are already expert!")


@bot.message_handler(content_types=['video'])
def set_expert_video(message):
    senders = models.Expert.query.filter_by(telegram_id=message.from_user.id)
    sender = senders.first()
    if (sender):
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(str(message.from_user.id)+'.mp4', 'wb') as new_file:
            new_file.write(downloaded_file)
#        sender.AboutLink = str(message.from_user.id)+'.mp4'
#        dbs.flush()        
#        dbs.commit()
#        expert = models.Expert.query.filter_by(telegram_id=message.from_user.id).first()
        bot.reply_to(message, "You About video saved: ")
    else:
        bot.reply_to(message, "I don't know what I should do!")
  
"""      
@bot.message_handler(regexp=YOUTUBE_URL_REGEXP)
def get_expert_by_link(message):
    experts = models.Users.query.filter_by(AboutLink=message.text)
    print str(message.text)
    print str(experts.count())
    if (experts.count() > 0):
        expert = experts.first()
        expert.ActiveUserId = message.from_user.id
        expert.UserChatId = message.chat.id
        dbs.flush()        
        dbs.commit()
        bot.reply_to(message, "Ask expert "+str(expert.FirstName)+" about "+message.text)
    else:
        bot.reply_to(message, "No such experts!")
"""    

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    bot.reply_to(message, "Some message")
"""
    # if message from expert than send message to user
    experts = models.Users.query.filter_by(TelegramId=message.from_user.id)
    if (experts.count() > 0):
        expert = experts.first()
        if (expert.ActiveUserId > 0):
            bot.send_message(expert.UserChatId, message.text)
        else:
            bot.reply_to(message, "First wait a question!")
    # if message from user than send message to expert
    else:
        experts1 = models.Users.query.filter_by(ActiveUserId=message.from_user.id)
        if (experts1.count() > 0):
            expert1 = experts1.first()
            bot.send_message(expert1.ExpertChatId, message.text)
        else:
            bot.reply_to(message, "First find the expert!")
"""           
#bot.polling()
           
# Remove webhook, it fails sometimes the set if there is a previous webhook           
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

#print WEBHOOK_SSL_CERT
#print WEBHOOK_SSL_PRIV

# Start flask server
if __name__ == "__main__":
    app.run()
#    app.run(host=WEBHOOK_LISTEN,
#            port=WEBHOOK_PORT,
#            ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
#            debug=True)
    