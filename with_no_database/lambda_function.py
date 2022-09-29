from toSlack import toSlack
from fromCrawling import fromCrawling
from datetime import datetime

class TblCrawlingData:
    def __init__(self, name, content, additional, startDate, link):
        self.name = name
        self.content = content
        self.additional = additional
        self.startDate = startDate
        self.link = link

if __name__ == "__main__":
        holaworld = fromCrawling()
        slack = toSlack()

        list = holaworld.holaworld_crawl()
        slack.sendToSlack(list)



#def lambda_handler(event, context):
#    holaworld = fromCrawling()
#    slack = toSlack()

#    list = holaworld.holaworld_crawl()
#    slack.sendToSlack(list)
    
