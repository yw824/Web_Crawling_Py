import slack_sdk

if __name__ == '__main__':
    SLACK_TOKEN = 'INPUT_TOKEN_HERE'
    SLACK_CHANNEL = '#INPUT_CHANNEL_HERE'
    message = 'TESTING MESSAGE FROM SLACK_BOT!!'

    client = slack_sdk.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel=SLACK_CHANNEL, text=message)