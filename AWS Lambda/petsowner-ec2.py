import json
import http.client

url = "54.92.182.247"
port = 8012


def lambda_handler(event, context):
    conn = None
    try:
        conn = http.client.HTTPConnection(url, port)

        # Extract the HTTP method and path parameters from the event
        method = event.get('httpMethod')
        path_parameters = event.get('pathParameters', {})
        pet_owner_id = path_parameters.get('petOwnerId')

        # Route the request based on the method and path
        if method == 'GET':
            path = f"/getowner/{pet_owner_id}" if pet_owner_id else "/"
            conn.request(method, path)
        elif method == 'POST' and event.get('path') == '/createpetowner':
            # Example body, adapt as needed
            body = json.dumps({
                "Name": "Steve",
                "Email": "steve@example.com",
                "Telephone": "123-456-789",
                "State": "StateName",
                "City": "CityName"
            })
            headers = {'Content-type': 'application/json'}
            conn.request(method, "/createpetowner", body, headers)
        elif method == 'PUT' and pet_owner_id:
            conn.request(method, f"/updatepetowner/{pet_owner_id}")
        elif method == 'DELETE' and pet_owner_id:
            conn.request(method, f"/deletepetowner/{pet_owner_id}")
        else:
            raise ValueError("Invalid request method or path")

        response = conn.getresponse()

        if response.status == 200:
            body = response.read().decode('utf-8')
            return {"statusCode": 200, "body": json.dumps(body)}
        else:
            return {"statusCode": response.status, "body": "Request failed with status code: " + str(response.status)}

    except Exception as e:
        print("Error occurred: ", e)
        return {"statusCode": 500, "body": "Internal server error"}

    finally:
        if conn:
            conn.close()

    return {"statusCode": 500, "body": "Internal server error"}
