import requests
import feedparser
import configuration
from twilio.rest import Client


class FeedHandler(object):
    def __init__(self, feed_url, programming_language, location):
        self.url = feed_url
        self.programming_language = programming_language
        self.location = location

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
        



def main():
    FH = FeedHandler('https://justjoin.it/feed', 'Python', 'Poznań')
    print(FH.entries_string_creating())
    #FH.twilio_sms_sender()

if __name__ == '__main__':
    main()
