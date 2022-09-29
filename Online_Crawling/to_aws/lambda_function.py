from Crawl import Crawl
from Slack import Slack

def lambda_handler():
    crawl = Crawl()
    slack = Slack()

    crawl.holaworld_Crawl()
    slack.toSlack()