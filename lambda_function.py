import json
import logging
import boto3

from boto3.dynamodb.conditions import Key, Attr
def lambda_handler(event, context):
    # TODO implement
    print (str(event))
    print (str(context))
    if event['key']:
        results = dbhandle(str(event['key']))
        a = [];
        for item in results:
            a.append(item["Name"])
    else:
        a = "";
    resp ={
        "statusCode": 200,
        "headers":{
            "Access-Control-Allow-Origin": "*",
        },
        "body": "hello:"+ str(a),
    }
    return resp;
    
def dbhandle(keyword):
    dynamodb = boto3.resource("dynamodb",region_name='us-east-1');
    table = dynamodb.Table('DB1');
    #response = table.query(
    #KeyConditionExpression=key('Name').eq('mike')
    #);
    response = table.scan(FilterExpression=Attr('Name').contains(keyword));
    items = response['Items'];
    return items
    

