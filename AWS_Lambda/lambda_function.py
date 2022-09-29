import json

def lambda_handler(event, context):
    # TODO implement - 이벤트가 발생하면 무조건 'Hello from Lambda'라는 메세지를 반환한다.
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# VSCode 커널에서 실행하면 실행되지 않는다. 
# 무조건 AWS Lambda 웹 서버 환경에서 실행해야 한다.
# 맨 처음에 기본적으로 제공하는 소스 코드의 모습
