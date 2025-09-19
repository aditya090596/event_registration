import boto3
import json

dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')
table = dynamodb.Table('eventmanagement')

def lambda_handler(event, context):
    # Parse request body
    body = json.loads(event.get("body", "{}"))
    cname = body.get("cname")
    cemail = body.get("cemail")
    eventid = body.get("eventid")
    eventname = body.get("eventname")

    # Save to DynamoDB
    table.put_item(
        Item={
            'eventid': eventid,
            'eventname': eventname,
            'cname': cname,
            'cemail': cemail
        }
    )

    # Send email via SES
    ses.send_email(
        Source="no-reply@yourdomain.com",  # verified sender
        Destination={"ToAddresses": [cemail]},
        Message={
            "Subject": {"Data": "Event Registration Confirmation"},
            "Body": {
                "Text": {
                    "Data": f"Hi {cname},\n\nYou have successfully registered for {eventname} (ID: {eventid})."
                }
            }
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({"message": "Registration successful!"})
    }
