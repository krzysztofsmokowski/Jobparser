import requests
import feedparser
import configuration
import telepot
import time
import logging
from twilio.rest import Client


class FeedHandler(object):
    def __init__(self, feed_url, programming_language, location):
        self.url = feed_url
        self.programming_language = programming_language
        self.location = location
        self.bot = telepot.Bot(configuration.telegram_auth)
        logging.getLogger().setLevel(logging.INFO)

    def entries_string_creating(self):
        feed = feedparser.parse(self.url)
        job_list = 'Jobs in {}: '.format(self.location)
        for entries in feed.entries:
            if self.programming_language in entries.title and self.location in entries.summary:
                job_list += entries.title + ' '
        return job_list

    def twilio_sms_sender(self):
        client = Client(configuration.account_sid, configuration.auth_token)
        message = client.messages.create(
                to=configuration.to,
                from_=configuration._from,
                body=self.entries_string_creating())
        return message.sid
        
    def telegram_sender(self):
        self.bot.sendMessage(configuration.telegram_id, str(self.entries_string_creating()))
        logging.info("message succesfuly sent")

    def jobs_string_compare(self):
        while True:
            str_of_jobs = str(self.entries_string_creating())
            time.sleep(3600)
            str_to_compare = str(self.entries_string_creating())
            if str_of_jobs == str_to_compare:
                pass
            else:
                self.telegram_sender()
                logging.info("new jobs appeared, message sent")

                
def main():
    FH = FeedHandler('https://justjoin.it/feed', 'Python', 'Poznań')
    print(FH.telegram_sender())
    FH.jobs_string_compare()

if __name__ == '__main__':
    main()
