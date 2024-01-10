import json
import boto3
from datetime import datetime

sns = boto3.client('sns')

def lambda_handler(event, context):
    # Error handling if the incoming event is not formatted as expected
    try:
        # Extract the message from the triggering SNS event
        incoming_message = event['Records'][0]['Sns']['Message']
    except (KeyError, IndexError):
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid SNS message format')
        }
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")

    # Including information from the triggering message and the current time
    outgoing_message = f"Received message: {incoming_message} at {current_time}"

    sns.publish(
        TopicArn="arn:aws:sns:us-east-1:555398594737:send",  # Replace with the ARN of the next topic
        Subject="Notification from Lambda",
        Message=outgoing_message
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Published to SNS: ' + outgoing_message)
    }
