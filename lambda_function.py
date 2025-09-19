import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    
    Cname = event.get("cname")
    Cemail    = event.get("cemail")
    Eventid   = event.get("eventid")
    EventName = event.get("eventname")

    # import to dynamo table
    boto3.resource("dynamodb").Table("eventmanagement").put_item(
        Item={"cname": Cname,
             "cemail": Cemail,
             "eventid": Eventid,
             "eventname": EventName
        
        }
    )
    # Send confirmation email via SES
    boto3.client("ses", region_name="ap-south-1").send_email(
        Source="user20@gmail.com",
        Destination={"ToAddresses": [Cemail]},
        Message={
            "Subject": {"Data": "Event Registration Confirmation"},
            "Body": {
                "Text": {"Data": f"Your registration for the event {EventName} has been confirmed."}
            }
        }
    )
    # return {
    #     "statusCode": 200,
    #     "headers": {
    #         "Access-Control-Allow-Origin": "*",  # replace with your frontend origin if needed
    #         "Access-Control-Allow-Methods": "POST,OPTIONS",
    #         "Access-Control-Allow-Headers": "Content-Type"
    #     },
    #     "body": json.dumps({"message": "Registration successful!"})
    # }  
    
