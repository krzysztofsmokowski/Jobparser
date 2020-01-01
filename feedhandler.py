import requests
import feedparser
import configuration
import telepot
import time
from datetime import datetime
import logging


class FeedHandler(object):
    def __init__(self, feed_url, programming_language, location):
        self.url = feed_url
        self.programming_language = programming_language
        self.location = location
        self.bot = telepot.Bot(configuration.telegram_auth)
        logging.getLogger().setLevel(logging.INFO)

    def entries_list_creating(self):
        feed = feedparser.parse(self.url)
        job_string = 'Jobs in {}: '.format(self.location)
        job_list = []
        for entries in feed.entries:
            if self.programming_language in entries.title and self.location in entries.summary:
                job_list.append(entries.title)
        job_list.sort()
        return job_list
        
    def telegram_sender(self):
        self.bot.sendMessage(configuration.telegram_id, 'Jobs in {} '.format(self.location) + str(self.entries_list_creating()))
        logging.info("message succesfuly sent")

    def jobs_list_compare(self):
        while True:
            list_of_jobs = self.entries_list_creating()
            time.sleep(2400)
            list_to_compare = self.entries_list_creating()
            if bool(set(list_of_jobs).intersection(list_to_compare)) == True:
                pass
            else:
                self.telegram_sender()
                logging.info("new jobs appeared, message sent")
                logging.info(datetime.now().isoformat(timespec='hours'))
                
def main():
    FH = FeedHandler('https://justjoin.it/feed', 'Python', 'Poznań')
    FH.jobs_list_compare()

if __name__ == '__main__':
    main()
