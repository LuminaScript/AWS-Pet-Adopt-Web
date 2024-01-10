import json

import http.client

url = "6156beanstalk-env.eba-r5bpgvxm.us-east-1.elasticbeanstalk.com"
port = 8012


def lambda_handler(event, context):
    print("event:")
    print(event)
    print("context: ")
    print(context)
    http_method = event.get('httpMethod')
    path = event.get('resource')  # or event.get('path')
    print("path:")
    print(path)
    print("http method:")
    print(http_method)

    # Handling GET request to root ('/')
    if path == '/' and http_method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps('Hello, World!')
        }

    # Handling GET request to '/Pets'
    elif path == '/Pets' and http_method == 'GET':
        return get_all_pets()

    # Handling PUT request
    elif path and path.startswith('/updatepetname') and http_method == 'PUT':
        new_name = event['queryStringParameters']['newname']
        pet_id = event['queryStringParameters']['id']
        # return update_pet_name(new_name)
        return update_pet_name(pet_id, new_name)
    # elif path == '/updatepetname' and http_method == 'PUT':
    # # elif path and path.startswith('/update_pet_name') and http_method == 'PUT':
    #     pet_id = event['queryStringParameters']['id']
    #     new_name = event['queryStringParameters']['newname']
    #     return update_pet_name(pet_id, new_name)

    # Handling DELETE request to '/delete/{id}'
    elif path and path.startswith('/delete/') and http_method == 'DELETE':
        pet_id = event['pathParameters']['id']
        return delete_pet(pet_id)





    # Handling POST request to '/create'
    elif path == '/create' and http_method == 'POST':
        # pet_data = json.loads(event.get('body', '{}'))
        name = event['queryStringParameters']['petBreed']
        category = event['queryStringParameters']['petCategory']
        breed = event['queryStringParameters']['petName']
        return create_pet(name, category, breed)

    else:
        return {
            'statusCode': 400,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps('Invalid request')
        }


def get_all_pets():
    conn = http.client.HTTPConnection(url, port)
    conn.request('GET', "/Pets")
    response = conn.getresponse()
    if response.status == 200:
        body = response.read().decode('utf-8')
        return {"statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps(body)}
    else:
        return {"statusCode": response.status,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": "Request failed with status code: " + str(response.status)}


def update_pet_name(pet_id, new_name):
    conn = http.client.HTTPConnection(url, port)
    conn.request('PUT', f"/update_pet_name/{pet_id}?name={new_name}")
    response = conn.getresponse()
    if response.status == 200:
        body = response.read().decode('utf-8')
        return {"statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps(body)}
    else:
        return {"statusCode": response.status,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": "Request failed with status code: " + str(response.status)}


def delete_pet(pet_id):
    conn = http.client.HTTPConnection(url, port)
    conn.request('DELETE', f"/delete/{pet_id}")
    response = conn.getresponse()
    if response.status == 200:
        body = response.read().decode('utf-8')
        return {"statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps(body)}
    else:
        return {"statusCode": response.status,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": "Request failed with status code: " + str(response.status)}


def create_pet(name, category, breed):
    conn = http.client.HTTPConnection(url, port)
    conn.request('POST', f"/create?name={name}&category={category}&breed={breed}")
    response = conn.getresponse()
    if response.status == 200:
        body = response.read().decode('utf-8')
        return {"statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps(body)}
    else:
        return {"statusCode": response.status,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": "Request failed with status code: " + str(response.status)}
