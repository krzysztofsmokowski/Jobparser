import requests
import feedparser
import configuration
import smtplib


class FeedHandler(object):
    def __init__(self, feed_url, programming_language, location):
        self.url = feed_url
        self.entries_dict = {}
        self.mail_pwd = configuration.pwd
        self.mail = configuration.mail
        self.mail_receiver = configuration.receiver_mail
        self.programming_language = programming_language
        self.location = location


    def entries_dict_creating(self):
        feed = feedparser.parse(self.url)
        job_list = 'Jobs in {}: '.format(self.location)
        for entries in feed.entries:
            if self.programming_language in entries.title and self.location in entries.summary:
                #self.entries_dict[entries.title] = entries.summary[len(entries.summary)-40:len(entries.summary)-5]
                job_list += entries.title
        return job_list


    def email_sending(self):
        '''
        Method for sending email with information about jobs
        '''
        content_to_send = self.entries_dict_creating()
        mail = smtplib.SMTP('smtp.gmail.com:587')
        mail.ehlo()
        mail.starttls()
        mail.login(self.mail, self.mail_pwd)
        mail.sendmail(self.mail, self.mail_receiver, content_to_send)
        mail.close()


def main():
    FH = FeedHandler('https://justjoin.it/feed', 'Python', 'Poznań')
    print(FH.entries_dict_creating())
    print(FH.email_sending())

if __name__ == '__main__':
    main()
