def lambda_handler(event, context):
    print("In lambda handler")
    
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Ryan Kroonenburg"
    }
    
    return resp