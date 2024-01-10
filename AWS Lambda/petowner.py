import json


def lambda_handler(event, context):
    http_method = event['httpMethod']
    path = event['path']
    path_parameters = event.get('pathParameters', {})

    try:
        if http_method == 'GET' and 'id' in path_parameters:
            # Handle GET request for /getowner/{id}
            return get_owner(path_parameters['id'])

        elif http_method == 'PUT' and 'id' in path_parameters:
            # Handle PUT request for /updatepetowner/{id}
            return update_owner(path_parameters['id'], event['body'])

        elif http_method == 'DELETE' and 'id' in path_parameters:
            # Handle DELETE request for /deletepetowner/{id}
            return delete_owner(path_parameters['id'])

        elif http_method == 'POST' and path.endswith('/createpetowner'):
            # Handle POST request for /createpetowner
            return create_owner(event['body'])

        else:
            return response('Unsupported method or path', 400)

    except Exception as e:
        return response(f'Error: {str(e)}', 500)


def get_owner(owner_id):
    # Logic to retrieve pet owner information
    # Replace this with actual logic to retrieve data
    return response(f'Get owner details for ID {owner_id}', 200)


def update_owner(owner_id, data):
    # Logic to update pet owner information
    # Replace this with actual logic to update data
    return response(f'Update owner details for ID {owner_id}', 200)


def delete_owner(owner_id):
    # Logic to delete pet owner
    # Replace this with actual logic to delete data
    return response(f'Delete owner with ID {owner_id}', 200)


def create_owner(data):
    # Logic to create a new pet owner
    # Replace this with actual logic to create data
    return response('Create a new pet owner', 200)


def response(message, status_code):
    return {
        'statusCode': status_code,
        'body': json.dumps({'message': message}),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

