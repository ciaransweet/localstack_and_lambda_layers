# Lambda Layers in LocalStack (The free version)

*Using the free version of LocalStack? Need to use Lambda Layers? Look no further!*

## Prequisites
* Python 3+
* Docker Compose

Install the required pip packages for the project with:
```
$ pip3 install -r requirements.txt
```

# Run LocalStack

Run the LocalStack container in the background with:
```
$ docker-compose up -d
# If you're a MacOS user like me, you might need to do:
$ mkdir lstmp
$ TMPDIR=./lstmp docker-compose up -d
```

After a while it will be ready, you can double check this by seeing if `Ready.` is in the logs:
```
$ docker logs -f localstack
...
...
Ready.
```

# Create the Layer, deploy the Lambda and test it:

```
$ cd lambda
$ bash test-lambda.sh
Build Layer and extract zip of dependencies
ac038acb524c360a5b8a4e47277abea58919e4ad2eaee33aed7c2b6c44b2fd92
-----------------------
Creating lambda layer
-----------------------
Remove lambda python packages
Remove useless files
Remove uncompiled python scripts
Strip shared libraries
Create archives
cogeo
cogeo
Unzip Layer and move all items up one directory
Copy in Lambda code and zip up new 'uber' Lambda
========= test session starts =========
platform darwin -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /Users/ciaran/dev/localstack_and_lambda_layers/lambda
collected 1 item                                                                                                                                                                                       

test_lambda.py .

========= 1 passed in 28.79s =========
```
