import time
import json
import boto3
import http.client

url = "52.90.97.138"


def lambda_handler(event, context):
    try:
        method = event.get('httpMethod')
        # Establish a connection to the server
        conn = http.client.HTTPConnection(url)

        # Send a GET request
        adopter_id = event.get('pathParameters')

        if method == 'GET':
            if adopter_id:
                # Handle request for a specific adopter
                conn.request(method, f"/adopter/{adopter_id}")
            else:
                # Handle request for all adopters
                conn.request(method, "/adopters")
        elif method == 'POST' and event.get('path') == '/adopter/create':
            # Example body, adapt as needed
            body = json.dumps({
                "name": "jason",
                "age": 11,
                "email": "czh2162216@gmail.com",
                "phone": "001-1101010"
            })
            headers = {'Content-type': 'application/json'}
            conn.request(method, "/adopter/create", body, headers)

        elif method == 'PUT' and adopter_id:
            conn.request(method, f"/adopter/{adopter_id}/update")

        elif method == 'DELETE' and adopter_id:
            conn.request(method, f"/adopter/{adopter_id}/delete")

        # Get the response from the server
        response = conn.getresponse()

        # Check if the request was successful (status code 200)
        if response.status == 200:
            print("Response from the server:")
            print(response.read().decode('utf-8'))
        else:
            print(f"Error: {response.status}")
    except http.client.HTTPException as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

    return {"statusCode": 200, "body": json.dumps("Run Successful")}