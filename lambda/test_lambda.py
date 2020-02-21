import json
from unittest import TestCase

import boto3


def get_lambda_client():
    return boto3.client('lambda',
                        aws_access_key_id='',
                        aws_secret_access_key='',
                        region_name='eu-west-2',
                        endpoint_url='http://localhost:4574')


def deploy_lambda():
    with open('lambda.zip', 'rb') as f:
        zipped_code = f.read()
    get_lambda_client().create_function(
        FunctionName='geo-lambda',
        Runtime='python3.7',
        Role='a-role',
        Handler='lambda.handler',
        Code={'ZipFile': zipped_code},
        Environment={
            'Variables': {
                'GDAL_DATA': '/opt/share/gdal',
                'PROJ_LIB': '/opt/share/proj'
            }
        }
    )


def invoke_lambda_and_get_response():
    return json.loads(get_lambda_client().invoke(
        FunctionName='geo-lambda',
        InvocationType='RequestResponse'
    )['Payload'].read().decode('utf-8'))


class Test(TestCase):
    def setup_method(self, method):
        deploy_lambda()

    def test_that_layer_works(self):
        resp = invoke_lambda_and_get_response()
        self.assertEqual(resp["message"], "Printed all versions")
