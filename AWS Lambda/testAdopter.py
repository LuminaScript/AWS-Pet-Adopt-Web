


import time
import json
import boto3



def lambda_handler(event, context):


    # boto3 client
    client = boto3.client("ec2")
    ssm = boto3.client("ssm")


    # getting instance information
    describeInstance = client.describe_instances()


    InstanceId = "i-02bd8a2bee2be424f"


    # command to be executed on instance
    print("before ssm.send_command")
    response = ssm.send_command(InstanceIds=[InstanceId],DocumentName="AWS-RunPowerShellScript", Parameters={"commands": ['& "C:\mypsscript\helloworld.ps1"']})
    print("after ssm.send_command")

    # fetching command id for the output
    command_id = response["Command"]["CommandId"]


    time.sleep(3)


    # fetching command output
    output = ssm.get_command_invocation(CommandId=command_id, InstanceId=InstanceId)
    print(output)


    return {"statusCode": 200, "body": json.dumps("Run Successful")}
